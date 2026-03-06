# What is a Tuple?
# A tuple is:
# Ordered
# Immutable
# Allows duplicates
# Indexable
# Faster than lists (slightly)

t = (10, 20, 30)

#Q Create a tuple of 5 numbers. Print the 3rd element.
tt = (1,2,3,4,5)
print(tt[2])

#Q Unpack (10, 20, 30) into three variables.
x,y,z = t
print(x,y,z)

#Q Write a function that returns (min, max) from a list.
def min_and_max(t):
    tt = sorted(t)
    maxx = tt[-1]
    minn = tt[0]
    return maxx,minn

max_val,min_val = min_and_max(tt)
print("Max value : ",max_val," Min value : ",min_val)



