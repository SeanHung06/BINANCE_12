import numpy as np
import pandas as pd
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import binance
import time
import datetime
from binance.client import Client
api_key = 'X2gxu22k9f1ehz8rCUNxgoSNa3g9wEQlUMQzjtLUNgPjWRMJI24pVSzE8M8ndHOQ'
api_secret = 'BjHCmtPE5ycruDj1vWhzw3UhDDqd84dVBGAgQJsO9gxux33DbIL9kYIN85q9ksv6'
client = Client(api_key, api_secret)
client = Client("api-key", "api-secret", {"verify": False, "timeout": 20})
klines = client.get_historical_klines('ETHUSDT', Client.KLINE_INTERVAL_1DAY, '01 Jan, 2019')

# use panda data frame to process the Kline data 
whole_df = pd.DataFrame(klines)

whole_df.columns = ['Open_time','open','high','low','close','volume','Close_time', 'Quote asset volume', 'number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']
whole_df = whole_df.drop_duplicates(subset=['Open_time'], keep=False)

# use lambda to  transfor tje timestamp to local time 
whole_df['Open_time_1']=whole_df['Open_time'].apply(lambda d: datetime.datetime.fromtimestamp(int(d)/1000).strftime('%Y-%m-%d %H:%M:%S'))
print(whole_df)

#use for loop to transfer the timestamp 
for i in whole_df.Open_time:
    timeArray = time.localtime(i/1000)
    #print(time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
    
#whole_df.Open_time= time.strftime("%Y-%m-%d %H:%M:%S",whole_df.Open_time.str)

whole_df.to_excel("binance_ETHUSDT_data.xlsx")
whole_df.to_csv('binance_ETHUSDT_data.csv', encoding='utf-8')


depth = client.get_order_book(symbol='BNBBTC')

#print(depth)

import csv
# open the CSV file
with open('./binance_ETHUSDT_data.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    #for row in rows:
        #print(row)

