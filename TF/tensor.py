from numpy.core.fromnumeric import ptp
import pandas as pd
import numpy as np

 
data = pd.read_csv('http://bit.ly/ld-sample-idol', index_col='순위')
print(data)
print('='*50)
print(data.head())
print('='*50)
print(data.iloc[3])
