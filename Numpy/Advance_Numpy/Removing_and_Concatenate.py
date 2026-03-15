'''
np.concatenate(( array1, array2 ), axis = None/0/1)


'''

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([7,8,9])

concat_arr = np.concatenate((arr1, arr2), axis=0)
print(concat_arr)


'''
np.delete( array, index, axis )

'''

arr3 = np.array([[11,22,33],[77,66,55]])
new_arr = np.delete(arr3, 1, axis=0)
print(new_arr)