#------ variables outside a function is global you can use it anywhere
x = 5 #------ global variable
def myfunc():
  print(x)
myfunc() #------ outputs 5

x = 'awesome'
def myfunc():
  x = 'fantastic'
  print('Python is ' + x) 
myfunc() #------ outputs python is fantastic
print('Python is ' + x) #------ outputs python is awesome

#------ hint: defining a function is asking what do you want the function name myfunc() to do and
#  to use it we invoke it which is calling the function
# when calling a function by the name we give it a parenthesis ()