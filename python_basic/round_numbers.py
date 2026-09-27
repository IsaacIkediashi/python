number = 12.34567

print(number) #------ outputs 12.34567
print(f'The number is ${number:.2f}') #------ outputs $12.35

# The . tells us after a decimal point
# The 2 tells how many digits we want shown after the decimal point
# The f tells python we want to display it as a fixed point number rather than a scientific notation e

#Rounding the number and placing the value in a variable there is a function for that called round()

number2 = round(number,3)
print(number2)

number = round(number,3)
print(number)

number3 = 12.3011
number4 = round(number3,2)
print(f'The number4 is ${number4}') #------ outputs The number4 is $12.3

# The use of a format specifier is better than a round function in the terms of a zero (0) in the decimal place
number3 = 12.3009
number4 = round(number3,3)
print(f'The number4 is ${number4}') #------ outputs The number4 is $12.301

number3 = 12.3009
number4 = round(number3,2)
print(f'The number4 is ${number4}') #------ outputs The number4 is $12.3

number3 = 12.3009
number4 = round(number3,1)
print(f'The number4 is ${number4}') #------ outputs The number4 is $12.3

# The best is using a format specifier rather than round() function that does not register the zeros after rounding
# the format specifier registers the zeros
print(f'The number4 is ${number4:.2f}') #------ outputs The number4 is $12.30




