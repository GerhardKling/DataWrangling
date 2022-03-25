"""
Download data from the web in Python
author: Data nerd
"""
import requests
import numpy as np
import pandas as pd


url = 'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/india-TAVG-Trend.txt'
response = requests.get(url, allow_redirects = True)
strings = response.text #takes strings
file_name = "output.txt"
open(file_name, 'w').write(strings)
data = np.loadtxt(file_name, comments = '%')
df = pd.DataFrame(data[:,:6], columns = ['year', 'month', 'm_ano', 'm_temp', 'a_ano', 'a_temp'])
print(df.head())



