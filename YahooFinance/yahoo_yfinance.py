"""
Data from Yahoo Finance

@author: GK
"""
import yfinance as yf
import matplotlib.pyplot as plt

#Specify start and end with format "YYYY-MM-DD"
#By default daily data; you can get intra-daily data; only last 30 days
# data = yf.download("GOOG", start = "2020-11-04", end = "2020-11-11", interval = "1m")
data = yf.download("BTC-USD", period = "1d", interval = "1m")

#DataFrame
print(type(data))

#Check data structure
print(data.head())

#Plot data
plt.plot(data.Close)

plt.show()
