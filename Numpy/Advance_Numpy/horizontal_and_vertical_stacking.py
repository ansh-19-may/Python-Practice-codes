'''
np.vstack(( array1, array2 ))   - making a 2D array vertical stack

np.hstack((array1 , array2 ))   - making a 1D array horizontal stack 
'''

import numpy as np 

arr1 = np.array([4,6,8])
arr2 = np.array([24,64,83])

print(f'vertical stacking  {np.vstack((arr1, arr2))}')

print(f'horizontal stacking  {np.hstack((arr1, arr2))}')
