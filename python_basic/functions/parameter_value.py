# The following example shows how to use a default parameter value

# If we call the function without argument, it uses the default value:

def my_function(country = 'Norway'):
  print('I am from ' + country)
my_function('Sweden') #------ outputs I am from Sweden
my_function('India') #------ outputs I am from India
my_function() #------ outputs I am from Norway
my_function('Brazil') #------ outputs I am from Brazil


# Passing a list as an argument

# You can send any data types of argument to a function (string,number,list,dictionary e.t.c.), and 
# it will be treated as the same data type inside the function.

# If you can send a list as an argument, it will still be a list when it reaches the function:

def my_function(food):
  for x in food:
    print(x)
fruits = ['apple','banana','cherry']
my_function(fruits) #------ outputs apple banana cherry

