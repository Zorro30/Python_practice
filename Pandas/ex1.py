# import pandas as pd

# data = pd.read_csv('Cloud_Cover.csv')

# print(data.head())




import numpy as np

import scipy

import scipy.signal
I = [[8, 6, 2, 7], 
     [6, 2, 4, 1],
     [5, 8, 5, 2],
     [3, 0, 3, 2]]
K = [[4, 3], 
     [7, 2]]
answer = scipy.signal.convolve2d(I, K, mode='valid')
print(answer)