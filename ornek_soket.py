import sqlite3
import json
from algolab import API
from ws import AlgoLabSocket
from config import *
import time
import pandas as pd
import os
import numpy as np
from datetime import datetime
df=pd.read_csv("df.csv")
hissem=df["Hisse"].unique()
for i in range(len(hissem)):
    hissem[i]=hissem[i][:-3]
db_file = "veriler6.db"


# Veritabanı bağlantısını oluştur
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Veritabanında tabloyu oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS veriler (
                    id INTEGER PRIMARY KEY,
                    symbol TEXT,
                    market TEXT,
                    price REAL,
                    high REAL,
                    low REAL,
                    date TEXT
                )''')

# Veritabanı bağlantısını commit et
conn.commit()



def process_msg(cursor, msg):
    try:
        content = msg["Content"]
             
        symbol = content["Symbol"]
        
        # Eğer symbol hissem arrayinde ise veriyi işle
        if symbol in hissem:
            market = content["Market"]
            price = content["Price"]
            high = content["High"]
            low = content["Low"]
            date = content["Date"]
            
            if market == "IMKBH":               
                cursor.execute('''INSERT INTO veriler (
                                    symbol, market, price, high, low, date
                                    ) VALUES (?, ?, ?, ?, ?, ?)''',
                                    (symbol, market, price, high, low, date))
                # Veritabanı bağlantısını commit et
                conn.commit()
                
    except Exception as e:
        print("Error processing message: ", e)

if __name__ == "__main__":

    algo = API(api_key=MY_API_KEY, username=MY_USERNAME, password=MY_PASSWORD, auto_login=True)
    soket = AlgoLabSocket(algo.api_key, algo.hash, "T")
    soket.connect()
    while not soket.connected:
        time.sleep(0.05)

    candle = algo.GetCandleData("XU100", "1")
    if candle:
        try:
            succ = candle["success"]
            if succ:
                ohlc = []
                content = candle["content"]
                for i in range(len(content)):
                    d = content[i]["date"]
                    try:
                        dt = datetime.strptime(d, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    except:
                        dt = datetime.strptime(d, "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m-%d %H:%M:%S")
                    o = content[i]["open"]
                    h = content[i]["high"]
                    l = content[i]["low"]
                    c = content[i]["close"]
                    ohlc.append([dt, o, h, l, c])
                endeks = pd.DataFrame(columns=["date", "open", "high", "low", "close"], data=np.array(ohlc))
                json_data=endeks.to_json(orient='records')
            else: print(candle["message"]) 
        except Exception as e:
            print(f"Hata oluştu: {e}")
    endeks.iloc[:,1:]=endeks.iloc[:,1:].astype(float)
    endeks=endeks.set_index(pd.to_datetime(endeks["date"]))
    del endeks["date"]
    endeks=endeks.resample('5T').last()
    endeks["Endeks Return"]=100*((endeks["close"]/endeks["close"].shift(1))-1)
    endeks=endeks.dropna()
    endeks.to_csv("endeks.csv")

    data = {"Type": "T", "Symbols": ["ALL"]}
    soket.send(data)
    

    
    while soket.connected:
        data = soket.recv()
        if data:
            try:
                msg = json.loads(data)
                process_msg(cursor, msg)
                    
            except:
                print("Error processing message")
                soket.close()
                break

   
    conn.close()
