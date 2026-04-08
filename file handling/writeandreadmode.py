'''
# 5  write and read- "w+"
 - if file is present then it opens the file in write mode and it will erase all the previous data in the file
 - if file is not present ,then it will create a new file wih the given name and extension
 - in w+ mode we are allowed to write into the file, as well as read from the file'''

f = open("file.txt","w+")
print(f.read())
f.close()
