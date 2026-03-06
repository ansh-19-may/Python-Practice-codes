num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : ")) 

print(f'Before swapping Num1 is {num1} and Num2 is {num2}')

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f'After swapping Num2 is {num1} and Num2 is {num2}')
