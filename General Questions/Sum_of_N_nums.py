#Sum of N numbers entered by user

nums = int(input("Enter count of numbers : "))
total = 0
for i in range(nums):
    n = int(input("Enter the number : "))
    total+= n

print("The sum is - ",total)