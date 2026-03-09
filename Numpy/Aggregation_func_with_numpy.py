'''
Some aggregation function are 

sum()
mean()
min()
max()
std()
var()
average()

'''

import numpy as np

arr = np.array([13, 56, 73, 25, 43, 21])

print(f' Sum of arr : {np.sum(arr)}')
print(f' Mean of arr : {np.mean(arr)}')
print(f' Minimun value in arr : {np.min(arr)}')
print(f' Maximum value in arr : {np.max(arr)}')
print(f' Standard deviation of arr : {np.std(arr)}')
print(f' Variance of arr : {np.var(arr)}')
print(f' Average of arr : {np.average(arr)}')