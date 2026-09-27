#------ Formatting strings used to display texts and variables together in your program
name = 'Bob'
age = 25

print(name) #------ outputs Bob
print(age)  #------ outputs 25

print(f'Your name is {name}') #------ outputs Your name is Bob
print(f'Your age is {age}')   #------ outputs Your age is 25

print(f'Hello {name}, you are {age} years old') #------ outputs Hello Bob, you are 25 years old

#------ string concatenation - combining two strings together
print('Hello, World! ' + 'I am Python') #------ outputs Hello, World! I am Python 

#------ f-strings are better than string cocatenation
name = 'Bob'
print('Hello, World! how are you doing today ' + name ) #------ outputs Hello, World! how are you doing today Bob
name = 'Bob'
print(f'Hello, World! how are you doing today {name}') 

#------ f-strings allows us put variables in our texts
#------ unlike string cocatenation, f-strings do not use the (+) operator
x = str(3) 
y = int(3)
z = float(3)

print(x) #----- outputs '3' 
print(y) #----- outputs  3
print(z) #----- outputs  3.0

#------ 3 is concatenated with other strings because it is a string
print('Joshua is ' + x + ' years old ' + 'Happy birthday!')  #------ outputs Joshua is 3 years old Happy birthday!

# note you can not mix strings and numbers during a maths operation or cocatenation,
# if you are using the (+) sign both values need to be the same

#F-string
name = "Bob"
print(f'Hello, World! how are you doing today {name}') #------ outputs Hello, World! how are you doing today Bob