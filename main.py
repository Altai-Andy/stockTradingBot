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
#print(AAPL)

#Visualize tha data
plt.figure(figsize=(12.5,4.5))
plt.plot(AAPL['Adj Close'], label='AAPL')
plt.title('Apple Adj. Close Price History')
plt.xlabel('17/6/2021 - 17/6/2021')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()
