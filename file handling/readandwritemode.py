'''
# 4  read and write - "r+"
- if file is exist then it opens the file in read mode and places the cursor at the begining of the file
- if file is not present ,then it will throw an error
- we are allowed to read from the file as wel as write into the file
- Note - the data will be overridden
'''

f = open("demo.txt","r+")


print(f.read())
print(f.tell())

f.seek(13)

f.write("something in between")

print(f.read())
print(f.tell())
f.seek(0)
f.write("one")
print(f.read())

# Pro tip : if you want to directly move the cursor into EOF , use 
f.seek(0,2)
print(f.tell())
f.close()