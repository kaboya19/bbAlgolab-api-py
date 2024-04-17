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
import numpy as np
import pandas as pd
import pandas as pd
from catboost import CatBoostRegressor
from algolab import API
from datetime import datetime
from config import *
import pandas as pd, numpy as np, json, os
import sqlite3
import pandas as pd
def fivemin():
   Conn = API(api_key=MY_API_KEY, username=MY_USERNAME, password=MY_PASSWORD, auto_login=True, verbose=True)
   db_file = 'C:\\Users\\Bora\\Documents\\GitHub\\bbAlgolab-api-py\\veriler6.db'
   conn = sqlite3.connect(db_file)
   cursor = conn.cursor()


   canlı=pd.read_sql_query("SELECT * FROM veriler", conn)
   canlı=canlı.dropna(axis=1)
   canlı=canlı.set_index(pd.to_datetime(canlı["date"]))
   canlı=canlı.groupby('symbol').resample('5T').last()
   del canlı["date"]
   del canlı["symbol"]
   canlı['prev_price'] = canlı.groupby('symbol')['price'].shift(1)
   canlı["Getiri"]=100*((canlı["price"]/canlı["prev_price"])-1)
   canlı=canlı.reset_index().dropna()
   canlı=canlı.set_index(pd.to_datetime(canlı["date"]))
   now = datetime.now()
    

   dakika = now.minute
    

   yuvarlanmis_dakika = (dakika // 5) * 5


   tarih=(now.strftime("%Y-%m-%d %H:") + "{:02d}".format(yuvarlanmis_dakika)+":00")
   endeks=pd.read_csv("C:/Users/Bora/Documents/GitHub/bbAlgolab-api-py/endeks.csv")
   endeks=endeks.set_index(pd.to_datetime(endeks["date"]))
   canlı["Endeks Return"]=0
   canlı["Endeks Return"].loc[tarih]=endeks["Endeks Return"].loc[tarih]

   canlı["DD"]=((canlı["price"]/canlı["high"])-1)*100
   canlı["Range"]=((canlı["high"]-canlı["low"])/canlı["price"])*100
   canlı.columns=["symbol","date","id","market","price","High","Low","prev_price","Getiri","Endeks Return","DD","Range"]

   X_test=canlı[["DD","Range","Endeks Return","Getiri"]]

   model=CatBoostRegressor(random_state=123)
   model.load_model("catboost_5m.bin")
   canlı["Tahmin"]=model.predict(X_test)
   canlı=canlı.sort_index()
   print(canlı.loc[tarih].sort_values(by="Tahmin",ascending=False).head(3)["symbol"].values)
   print(canlı.index[-1])



if __name__ == "__main__":
    fivemin()
