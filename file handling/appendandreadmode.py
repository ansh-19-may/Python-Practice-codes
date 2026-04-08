'''
# 6 append and read- "a+"
- if file is present then it opens the file in append mode and it will place the cursor end of the file
- if file is not present ,then it will create a new file wih the given name and extension
- in append and read mode we are allowed to write into the file as well as read from the file
- seek() - it will no be applicable'''

f = open("file.txt", "a+")

print(f.tell())

f.write("Write in the file using a+ mode")
f.seek(0)
print(f.read())
