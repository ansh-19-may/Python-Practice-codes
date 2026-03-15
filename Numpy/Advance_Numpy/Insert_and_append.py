'''

.insert( array, index, value, axis )
array - on which array value is inserting.
index - on which index
value - element to be inserted
axis  - if 0 then value is added row wise , if 1 then value is added col wise

'''

import numpy as np
# 1D insertion
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)
new_arr = np.insert(arr, 3, 55, axis=0)
print(new_arr)

# 2D insertion
arr_2d = np.array([[1,2], [2,3], [4,5]])
print(arr_2d)
new_2d_arr = np.insert(arr_2d, 1, [6,7],axis=0)
print(new_2d_arr)


 