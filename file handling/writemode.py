'''
# 2 write mode - "w"
- if file is present then it opens the file in write mode and it will erase all the previous data in the file
- if file is not present ,then it will create a new file wih the given name and extension
- in write mode we are allowed to write into the file, but we are not allowed to read from the file
'''


f = open("demo.txt", "w")

f.write("the previous data is removed and this is updated into the given file")

#we can't read data while in WRITE mode.
print(f.read())

f.close()