import numpy as np

# 1-D array 
arr = np.array([1,2,3,4])
print(arr)

# 2-D array
arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)


# To print the data type of array   ->  .dtype    -- property
print(f'the data type is  : {arr_2d.dtype}')

#To get the dimension of array  ->  .ndim -- property
print(f'the matrix {arr_2d} has dimension - {arr_2d.ndim}')


#To get no of rows and cols  ->   .shape   --  property
print(f'No of Rows and Cols : {arr_2d.shape}')


#To get no of element present  ->   .size   --  property
print(f'No of Elements present : {arr_2d.size}')


#To print matrix having 1's as elements  ->   .ones((rows,cols))
ones_arr = np.ones((3,3))
print(f'The one element matrix :\n  {ones_arr}')


#To print matrix having 0's as elements  ->   .zeros((rows,cols))
zeros_arr = np.zeros((2,3))
print(f'The zero element matrix :\n  {zeros_arr}')


#To print matrix having any no. (e.g.  3,4,5,7,8 etc ) as elements  ->   .full(shape, value)
filled_arr = np.full((3,3), 8)
print(f'The element matrix :  {filled_arr}')


# To print a sequence of number as a Numpy array   ->  .arange(start,stop,step)
seq_arr = np.arange(1,10,2)
print(seq_arr)


# To print Identity Matrix   ->  .eye(size)  size: NxM matrix
identity = np.eye(3)
print(f'Identity Matrix :\n {identity}')


# To Change the data type of elements in numpy array to another data type
# .astype(data type to be change)

float_arr = np.array([12.34, 4.5, 67.77])
int_arr = float_arr.astype(int)
print(f'we converted float element {float_arr}  into int element array {int_arr}')