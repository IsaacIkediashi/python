# A function is a block of code which only runs when it is called.

# In python a function is defined using the def keyword:

def myfunction():
  print('Hello from a function')

myfunction() #----- outputs Hello from a function

# Arguments

# information can be passed into functions as arguments, arguments are specified after the function name, inside the
#parenthesis.

#note - you can add as many arguments as you want, just seperate them with comma


def my_function(fname):
  print(fname + 'Refsnes')

my_function('Emil')  #------ outputs Emil Refsnes
my_function('Tobias')#------ outputs Tobias Refsnes
my_function('Linus') #------ outputs Linus Refsnes

#arguments are often shortened to args in python documentations

#note that you can pass data, known as parameters into a function

# Parameters or Arguments - the terms parameter and argument can be used for the same thing:
# information that are passed into a function.


# From a function's perspective:

#a paramether is a variable listed inside the paranthesis in the function definition.
#an argument is the value that is  sent to the function when it is called.



  



