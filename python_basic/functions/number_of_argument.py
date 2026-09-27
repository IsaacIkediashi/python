# Number of Arguments

# By default, a function must be called with the correct number of arguments - meaning that if your function 
# expects 2 arguments, not more, and not less.

# This function expects 2 arguments, and gets 2 arguments:

def my_function(fname,lname):
  print(fname + ' ' + lname)
my_function('Emil','Refsnes') #------ outputs Emil Refsnes

# If you try to call the function with 1 or 3 arguments, you will get an error:

#This function expects 2 arguments, but gets only 1:

def my_function(fname,lname):
    print(fname + ' ' + lname)
my_function('Emil') #------- outputs error