import numpy as np
import pandas as pd

# Series is a 1D vertical array and having indexes as LABELS
labels = ['a','b','c']


# A) Creating series using a list
my_list = [12,34,56]
ser_of_list = pd.Series(my_list,index=labels)# passing indexes from labels list for elements of list
print(f'list as a series\n{ser_of_list}')

# B) Creating series using numpy array

arr = np.array([45,67,89])
ser_of_np_arr = pd.Series(arr)
print(f'numpy array as series\n {ser_of_np_arr}')

# C) Creating series using a dictionary
my_dict = {'a':10,'b':30,'c':70}
ser_of_dict = pd.Series(my_dict) # WHILE CREATING SERIES FROM DICT , LABELS ARE CREATED WITH DICT KEYS.
print(f' dict as a series\n  {ser_of_dict}')
