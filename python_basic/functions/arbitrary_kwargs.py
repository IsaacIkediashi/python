#If you do not know how many keyword arguments that will be passed into your function, add two asterisk:
# (**) before the parameter name in the function definition.

#This way the function will receive a dictionary of arguments, and can access the items accordingly:

# If the number of keyword arguments is unknown, add a double (**) before the parameter name:

def my_function(**kids):
  print('His last name is ' + kids['lname'])
my_function(fname = 'Tobias', lname = 'Refsnes') #------ outputs His last name is Refsnes 

# Arbitary kwarg arguments are often shortened to **kwargs in python documentations.


# Parameter             Argument            
# kid                   Tobias
#*kids                  Tobias,Linus