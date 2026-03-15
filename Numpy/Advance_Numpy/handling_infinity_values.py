'''
np.isinf(arr)  : return list of boolean values and TRUE denotes a INFINITE VALUE is present in the array

np.nan_to_num( array, posinf=1000, neginf=-2000 )

'''

import numpy as np 
arr = np.array([10, 20, 30, np.inf, -np.inf, 12, np.nan])

print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf= 100, neginf=-100 , nan=10000)
print(cleaned_arr)