import sqlite3
import json
from algolab import API
from ws import AlgoLabSocket
from config import *
import time

# SQLite veritabanı dosyasının adı
db_file = "veriler1.db"

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Veritabanında tabloyu oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS veriler (
                    id INTEGER PRIMARY KEY,
                    symbol TEXT,
                    market TEXT,
                    price REAL,
                    change REAL,
                    ask REAL,
                    bid REAL,
                    date TEXT,
                    change_percentage REAL,
                    high REAL,
                    low REAL,
                    trade_quantity REAL,
                    direction TEXT,
                    ref_price REAL,
                    balance_price REAL,
                    balance_amount REAL,
                    buying TEXT,
                    selling TEXT
                )''')

# Veritabanı bağlantısını kapat
conn.commit()
conn.close()

def process_msg(msg):
    try:
        content = msg["Content"]
             
        symbol = content["Symbol"]
        market = content["Market"]
        price = content["Price"]
        change = content["Change"]
        ask = content["Ask"]
        bid = content["Bid"]
        date = content["Date"]
        change_percentage = content["ChangePercentage"]
        high = content["High"]
        low = content["Low"]
        trade_quantity = content["TradeQuantity"]
        direction = content["Direction"]
        ref_price = content["RefPrice"]
        balance_price = content["BalancePrice"]
        balance_amount = content["BalanceAmount"]
        buying = content["Buying"]
        selling = content["Selling"]
        if symbol=="EREGL":                
           conn = sqlite3.connect(db_file)
           cursor = conn.cursor()
           cursor.execute('''INSERT INTO veriler (
                                symbol, market, price, change, ask, bid, date, change_percentage,
                                high, low, trade_quantity, direction, ref_price, balance_price,
                                balance_amount, buying, selling
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                (symbol, market, price, change, ask, bid, date, change_percentage,
                                high, low, trade_quantity, direction, ref_price, balance_price,
                                balance_amount, buying, selling))
           conn.commit()
           conn.close()
    except Exception as e:
        print("Error processing message: ", e)

if __name__ == "__main__":
    algo = API(api_key=MY_API_KEY, username=MY_USERNAME, password=MY_PASSWORD, auto_login=True)
    soket = AlgoLabSocket(algo.api_key, algo.hash, "T")
    soket.connect()
    while not soket.connected:
        time.sleep(0.05)

    data = {"Type": "T", "Symbols": ["ALL"]}
    soket.send(data)
    while soket.connected:
        data = soket.recv()
        if data:
            try:
                msg = json.loads(data)
                process_msg(msg)
            except:
                print("Error processing message")
                soket.close()
                break
