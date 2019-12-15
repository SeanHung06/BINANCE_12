import numpy as np
import pandas as pd
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import binance
import time
from binance.client import Client
api_key = 'X2gxu22k9f1ehz8rCUNxgoSNa3g9wEQlUMQzjtLUNgPjWRMJI24pVSzE8M8ndHOQ'
api_secret = 'BjHCmtPE5ycruDj1vWhzw3UhDDqd84dVBGAgQJsO9gxux33DbIL9kYIN85q9ksv6'
client = Client(api_key, api_secret)
client = Client("api-key", "api-secret", {"verify": False, "timeout": 20})
klines = client.get_historical_klines('ETHUSDT', Client.KLINE_INTERVAL_1DAY, '01 Nov, 2019')

# use panda data frame to process the Kline data 
whole_df = pd.DataFrame(klines)
whole_df.columns = ['Open_time','open','high','low','close','volume','Close_time', 'Quote asset volume', 'number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']
#whole_df = whole_df.drop_duplicates(subset=['Open_time'], keep=False)
#print(whole_df)
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



client.ping()
time_res = client.get_server_time()
timeArray = time.localtime(time_res1)
print(timeArray)
products = client.get_products()
#print(products)

from binance.client import Client


api_key = 'xxx'
api_secret = 'xxx'
client = Client(api_key, api_secret)
import time
localTime = time.localtime()
print (localTime)
"""
for i in range(1, 10):
    local_time1 = int(time.time() * 1000)
    server_time = client.get_server_time()
    diff1 = server_time['serverTime'] - local_time1
    local_time2 = int(time.time() * 1000)
    diff2 = local_time2 - server_time['serverTime']
    print("local1: %s server:%s local2: %s diff1:%s diff2:%s" % (local_time1, server_time['serverTime'], local_time2, diff1, diff2))
    time.sleep(2)
"""
