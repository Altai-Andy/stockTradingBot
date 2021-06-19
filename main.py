# Description: This program uses the dual moving average crossover to determine when to buy and sell stock
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
#plt.style.use('fivethirteight')

#Load the data
#from google.colab import files
#uploaded = files.upload(AAPL.csv)

#Store the data
AAPL = pd.read_csv('AAPL.csv')
#Show the data
print(AAPL)



#Create the simple moving average with a 30 day window
SMA30 = pd.DataFrame()
SMA30['Adj Close'] = AAPL['Adj Close'].rolling(window=30).mean()
#print(SMA30)

#Create the simple moving average with a 100 day window
SMA100 = pd.DataFrame()
SMA100['Adj Close'] = AAPL['Adj Close'].rolling(window=100).mean()
#print(SMA100)


#Create a new data frame to store all the data
data = pd.DataFrame()
data['AAPL'] = AAPL['Adj Close']
data['SMA30'] = SMA30['Adj Close']
data['SMA100'] = SMA100['Adj Close']


#Create a function to signal when to buy and sell the asset/stock
def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []

    for i in range(len(data) -1 ):
        #Problem is here
        if data['AAPL'][i + 1] > data['AAPL'][i]:
            sigPriceBuy.append(data['AAPL'][i])
            sigPriceSell.append(np.nan)
        elif data['AAPL'][i + 1] < data['AAPL'][i]:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(data['AAPL'][i])
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    return (sigPriceBuy, sigPriceSell)
#Store the buy and sell data into a variable
buy_sell = buy_sell(data)
print(buy_sell)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[0]
#Visualize tha data and strategy to buy and sell stock
plt.figure(figsize=(12.6, 4.6))
plt.plot(AAPL['Adj Close'], label='AAPL', alpha = 0.35)
#plt.plot(SMA30['Adj Close'], label='SMA30', alpha = 0.35)
#plt.plot(SMA100['Adj Close'], label='SMA100', alpha = 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label='Buy', marker='^', color='green')
plt.scatter(data.index, data['Sell_Signal_Price'], label='Sell', marker='v', color='red')
plt.title('Apple Adj. Close Price History')
plt.xlabel('17/6/2021 - 17/6/2021')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

print(data)

