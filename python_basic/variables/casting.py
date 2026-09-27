x = 5 #------ this a variable with te value of a string.
y = "John" #------ this is a variable with the value of a number.
print(type(x)) #------ outputs <class 'str'>

print(type(y)) #------ outputs <class 'str'>

# specify the data type of a variable i.e it's value
x = str(3) 
y = int(3)
z = float(3)

print(x) #----- outputs '3' (python stores the number 3 as a string, changing it's original data type)
print(y) #----- outputs  3
print(z) #----- outputs  3.0

#------ 3 can be concatenated with other strings
print('Joshua is ' + x + ' years old')  #------ outputs Joshua is 3 years old

#------ numbers can not be cocatenated with strings
x = 3
print('Joshua is ' + x + ' years old') #------ error