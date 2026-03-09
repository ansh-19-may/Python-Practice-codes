import numpy as np 

# To reshape the given , changing the dimensions of array   .reshape(row,col)
arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
print(f'reshaped array : {reshaped_arr} ')
print(arr)


#FLATTENING 
# .ravel() -> give VIEW as a result. means it affects the real array
# .flatten()  -> give COPY as a result. means it does not affects the real array

arr_flt = np.array([[12,13,14],[45,78,90]])
print(arr_flt.ravel())     # modifies the real data , it don't create a copy.
print(arr_flt.flatten())   # not modies the real data, it give copy of data.