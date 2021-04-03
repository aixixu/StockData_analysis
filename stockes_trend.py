import time
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
font = {'family':'SimHei', 'weight':'bold', 'size':'12'}
plt.rc('font', **font)
plt.rc('axes', unicode_minus = False)
gafataDict = {'Google':'GOOG', 'Amazon':'AMZN', 'Facebook':'FB', 'Apple':'AAPL', 'Tesla':'TSLA', 'Maotai':'600519.SH', 'Alibaba':'BABA', 'Tencent':'0700.hk'}
start_date = '2018- 01 - 01' # start date
end_data = time.strftime('%Y-%m-%d') # grab the current date
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

# scatter
plt.rcParams['font.size'] = 15
ALbbDF.plot(x = 'Volume', y = 'Close', kind = 'scatter')
plt.xlabel('Volume',fontsize = 12)
plt.ylabel('Price($)',fontsize = 12)
