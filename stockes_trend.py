import time
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
from get_exchange_rate import get_exchange_rate
font = {'family':'SimHei', 'weight':'bold', 'size':'12'}
plt.rc('font', **font)
plt.rc('axes', unicode_minus = False)
gafataDict = {'Google':'GOOG', 'Amazon':'AMZN', 'Facebook':'FB', 'Apple':'AAPL', 'Tesla':'TSLA', 'Maotai':'600519.SS', 'Alibaba':'BABA', 'Tencent':'0700.hk'}
start_date = '2018- 01 - 01' # start date
end_data = time.strftime('%Y-%m-%d') # grab the current date

# Analyze Alibaba
ALbbDF = data.get_data_yahoo(gafataDict['Alibaba'],start_date,end_data)
ALbbDF.tail()
ALbbDF.index
ALbbDF.info()
ALbbDF.dtypes
ALbbDF.describe()
ALbbDF['DayHL'] = ALbbDF.eval('High-Low')
ALbbDF.tail()
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams["figure.figsize"] = (20,10)
ALbbDF.plot(y = 'Close' ,fontsize = 10)
plt.xlabel('Time',fontsize = 12)
plt.ylabel('Price($)',fontsize = 12)
plt.title('Alibaba stock price trend since 2018')
plt.grid()
plt.show()

# Plot scatter
plt.rcParams['font.size'] = 15
ALbbDF.plot(x = 'Volume', y = 'Close', kind = 'scatter')
plt.xlabel('Volume',fontsize = 12)
plt.ylabel('Price($)',fontsize = 12)
plt.title('Volume and Price')
plt.show()

ALbbDF.corr()

# Calculate exchange rate
exchange_cny_usd = float(get_exchange_rate('CNY','USD'))
exchange_hkd_usd = float(get_exchange_rate('HKD','USD'))
# Get 8 companies stock datafram
GoogleDF = data.get_data_yahoo(gafataDict['Google'],start_date,end_data)
AmazonDF = data.get_data_yahoo(gafataDict['Amazon'],start_date,end_data)
FacebookDF = data.get_data_yahoo(gafataDict['Facebook'],start_date,end_data)
AppleDF = data.get_data_yahoo(gafataDict['Apple'],start_date,end_data)
TeslaDF = data.get_data_yahoo(gafataDict['Tesla'],start_date,end_data)
MaotaiDF = data.get_data_yahoo(gafataDict['Maotai'],start_date,end_data)
TencentDF = data.get_data_yahoo(gafataDict['Tencent'],start_date,end_data)
# Change to USD
TencentDF['Close_dollar'] = TencentDF['Close'] * exchange_hkd_usd
MaotaiDF['Close_dollar'] = MaotaiDF['Close'] * exchange_cny_usd
# Plot 8 companies stock price trend since 2018
ax1 = GoogleDF.plot(y = 'Close', label = 'Google')
AmazonDF.plot(ax = ax1, y = 'Close', label= 'Amazon')
FacebookDF.plot(ax = ax1, y = 'Close', label= 'Facebook')
AppleDF.plot(ax = ax1, y = 'Close', label= 'Apple')
TeslaDF.plot(ax = ax1, y = 'Close', label= 'Tesla')
MaotaiDF.plot(ax = ax1, y = 'Close_dollar', label= 'Maotai')
ALbbDF.plot(ax = ax1, y = 'Close', label= 'Alibaba')
TencentDF.plot(ax = ax1, y = 'Close_dollar', label= 'Tencent')
plt.xlabel('Time')
plt.ylabel('Price($)')
plt.title('8 companies stock price trend since 2018')
plt.legend(loc=7, bbox_to_anchor=(1.111, 0.5))
plt.show()

# Compare the average stock price  of 8 companies
MeanList = [GoogleDF['Close'].mean(),AmazonDF['Close'].mean(),FacebookDF['Close'].mean(),AppleDF['Close'].mean(),TeslaDF['Close'].mean(),MaotaiDF['Close_dollar'].mean(),ALbbDF['Close'].mean(),TencentDF['Close_dollar'].mean()]

MeanSer = pd.Series(MeanList, index = ['Google', 'Amazon', 'Facebook', 'Apple','Tesla','Maotai', 'Alibaba', 'Tencent'])

MeanSer.plot(kind = 'bar', label = 'GAFATA')
plt.title('8 companies average stock price since 2018')
plt.xlabel('Companies name')
plt.ylabel('Average Price($)')
plt.xticks(rotation = 30)
plt.show()
