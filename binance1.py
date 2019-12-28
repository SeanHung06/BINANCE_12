import numpy as np
import pandas as pd
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import binance
import time
import datetime
from binance.client import Client
import matplotlib.pyplot as plt
import csv

#constant
api_key = 'hVvOTPoDT54u8CndCxam03axcJcaPZjWFAQv7wruzhK2PTeu80nt6mRkAeNkSAR9'
api_secret = 'E0PupiP3L94PxiWI0C6BUhzbLhLGwdHbroOUnB8lKyawmrEmWU5lasFndzHYSbCa'
client = Client(api_key, api_secret)
client = Client("api-key", "api-secret", {"verify": False, "timeout": 20})
klines = client.get_historical_klines('ETHUSDT', Client.KLINE_INTERVAL_1DAY, '10 Dec, 2019')
signal = 0 
#constant


trade_price = client.get_recent_trades(symbol='ETHUSDT')[250]['price']
trade_time = client.get_recent_trades(symbol='ETHUSDT')[250]['time']
trades = client.get_recent_trades(symbol='ETHUSDT')
#get server time
Server_time = client.get_server_time()
#print(Server_time)
lambda Server_time: datetime.datetime.fromtimestamp(int(Server_time)/1000).strftime('%Y-%m-%d %H:%M:%S')
#print(Server_time)
print(trade_price,trade_time)
trades_df = pd.DataFrame(trades)
#trades_df.to_excel("trades_df.xlsx")
trades_df.to_csv('trades_df.csv', encoding='utf-8')



# Create a Numpy array for trade price and trade time
arr = np.array([trade_price,trade_time])
np.savetxt('trade_details.csv', [arr], delimiter=',', fmt='%s')




# use panda data frame to process the Kline data 
whole_df = pd.DataFrame(klines)

whole_df.columns = ['Open_time','open','high','low','close','volume','Close_time', 'Quote asset volume', 'number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']
whole_df = whole_df.drop_duplicates(subset=['Open_time'], keep=False)

# use lambda to  transfor tje timestamp to local time 
whole_df['Open_time_GST']=whole_df['Open_time'].apply(lambda d: datetime.datetime.fromtimestamp(int(d)/1000).strftime('%Y-%m-%d %H:%M:%S'))


#get the Moving average for 7 days 15 days 30 days
whole_df['MA_1'] = whole_df['close'].rolling(1).mean()
whole_df['MA_2'] = whole_df['close'].rolling(2).mean()
whole_df['MA_7'] = whole_df['close'].rolling(7).mean()
whole_df['MA_15'] = whole_df['close'].rolling(15).mean()
whole_df['MA_30'] = whole_df['close'].rolling(30).mean()


#get the Exponetial Moving average for 7 days 15 days 30 days

whole_df['EMA_1'] = whole_df['close'].ewm(span=1).mean()
whole_df['EMA_2'] = whole_df['close'].ewm(span=2).mean()
whole_df['EMA_12'] = whole_df['close'].ewm(span=12).mean()
whole_df['EMA_26'] = whole_df['close'].ewm(span=26).mean()


whole_df['DIF'] = whole_df['EMA_12'] - whole_df['EMA_26']
whole_df['DEM'] = whole_df['DIF'].ewm(span=9).mean()
whole_df['OSC'] = whole_df['DIF'] - whole_df['DEM']



# drawing the plots for the EMA
fig,ax = plt.subplots(5,1,figsize=(10,10))
plt.subplots_adjust(hspace=0.5)
whole_df['EMA_1'].plot(ax=ax[0])
whole_df['EMA_26'].plot(ax=ax[1])
plt.plot(whole_df['Open_time_GST'],whole_df['EMA_1'])

ax[0].legend()
ax[1].legend()
#plt.show() 


EMA1 = whole_df['EMA_1'][whole_df['EMA_1'].size-1]
EMA2 = whole_df['EMA_2'][whole_df['EMA_2'].size-1]

data = open('data.txt', 'r')


signal_temp = data.read()
if EMA1 > EMA2 or EMA1 < EMA2:
    signal = 1
    data = open('data.txt', 'w')
    data.write(str(signal))
    data.close()

if(int(signal_temp) != signal):
    email_data = open('email_send_signal.txt', 'w')
    email_data.write(str(1))
    print(signal_temp,signal)

    
#drop the rest columns
whole_df= whole_df.drop(columns=['Ignore', 'Open_time'])
#print(whole_df)

#whole_df.to_excel("binance_ETHUSDT_data.xlsx")
whole_df.to_csv('binance_ETHUSDT_data.csv', encoding='utf-8')



