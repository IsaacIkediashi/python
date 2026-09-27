#------ if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass

#------ having an empty if statement like this will raise an error without the pass statement and 
# every code written under it will raise an error without indentation

c = 45
d = 709

if c < d:  #------ outputs an error

 e = 30
 f = 450

 if e > f:
   pass

