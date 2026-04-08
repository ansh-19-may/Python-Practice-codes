'''# 3 append mode - "a"
- if file is present then it opens the file in append mode and it will place the cursor end of the file
- if file is not present ,then it will create a new file wih the given name and extension
- in append mode we are allowed to write into the file but we are not allwed to read from the file
- seek() - it will no be applicable'''


f = open("appendtxt.txt","a")

print(f.tell())

f.close()
#here seek() method is not applicable. as we know append mode always need to put the cursor in the end.