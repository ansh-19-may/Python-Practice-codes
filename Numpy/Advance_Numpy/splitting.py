'''
np.split()  - equally split

np.hsplit() - horizontal split

np.vsplit() - vertical split
'''

import numpy as np

#split()
arr = np.array([12,56,873,5,7])
print(np.split(arr,5))

#vsplit()
arr2 = np.array([[1,2,3],[4,5,6]])
print(np.vsplit(arr2,2))

#hsplit()
arr3 = np.array([[11,44,66],[55,44,22]])
print(np.hsplit(arr3,3))
