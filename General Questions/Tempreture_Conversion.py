temp_cel = float(input("Enter Tempreture in Celsius"))
convert_fah = temp_cel * 1.8 + 32

temp_fah = float(input("Enter Tempreture in Fahrenheit"))
convert_cel = (temp_fah - 32)/1.8

print(f'the temp in Celcius {temp_cel} in Fahrenheit is {round(convert_fah,2)}')
print(f'the temp in Fahrenheit {temp_fah} in Celcius is {round(convert_cel,2)}')