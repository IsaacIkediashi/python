# To let a function return a value, use the return statement:

def my_function(x):
  return 5*x
my_function(3) #------ returns the value of 15
my_function(5) #------ returns the value of 25
my_function(9) #------ returns the value of 45

print(my_function(3)) #------ outputs 15
print(my_function(5)) #------ outputs 25
print(my_function(9)) #------ outputs 45



#return passes values into variables or functions
def my_function():
  return 30        #------ my_function() = 30

my_function() #------ returns the value of 30



#*declaring it by writing return e.g return double_value - The variable doule_value
user_input = int(input('What is the number to be increased: '))
double_value = user_input * 2

def my_func():
  return double_value 

print(my_func()) #------ outputs

# The function now carries the value of the variable i.e the function is a value which can be passed on to another
#variable.

