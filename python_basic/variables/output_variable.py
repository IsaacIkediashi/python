#------ for strings use the (+) character to add a variable to another variable 
#------ string cocatenation
x = 'awesome'
print('python is ' + x) #------ outputs python is awesome

x = 'python is '
y = 'awesome'
print(x + y) #------ outputs python is awesome

x = 'python is '
y = 'awesome'
z = x + y
print(z) #------ outputs python is awesome 

#------ for numbers the (+) character works as a mathematical operator
x = 5
y = 10
print(x + y) #------ outputs 15

# If you try to combine a string and a number python will give you an error
x = 5
y = 'John'
print(x + y) #error

