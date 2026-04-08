'''# 1 read mode - "r"
- if file is present/exist then it opens the file in read mode and places the cursor at the begining of the file
- if file is not present ,then it will throw an error
- in read mode we can **only** read from the file but we can not write into the file
- Default mode is read mode
'''

# to open file in read mode
f = open("read.txt", "r")

print(f.read())

#if you're going to write anything in this mode . it will throw an exception
#f.write("writing using read mode")

#to get the location of cursor
print(f.tell())

#always close the file object
f.close()