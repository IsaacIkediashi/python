# You can loop through a list using a for loop

thisList = ['apple','banana','cherry']

for fruit in thisList:    #------ for each item in this list execute a set of statements for each item - print, e.t.c.
#python stops the for loop when it runs an extra check for an item in the list if not stop list is finished, 
# even after printing the last item.
  
  print(fruit) #------ outputs apple banana cherry




# You can also loop through the list items by referring to their index number:
 

#Loop through the index numbers
#Use the range() and len() functions

#------ print all items by referring to their index number:

thisList = ['apple','banana','cherry']

for i in range(len(thisList)):
  print(thisList[i]) #------ outputs apple banana cherry

#the iterable created in the example above is [0,1,2].

#OR

thisList = ['apple','banana','cherry']
variable_range = range(len(thisList))

for i in variable_range:
  print(thisList[i]) #------ outputs apple banana cherry

#range creates a set of values which is a list of indexes - [0,1,2,3] or [0,1,2,3 and so on] or [1,2,3,4,5,...20,30,40] or [0,2,4,5,6... and e.t.c.]
thisList = [1,2,3,4,5]
variable_range = range(len(thisList))

for i in variable_range:
  print(thisList[i]) #------ outputs 1 2 3 4 5


thisList = [1,2,3,4,5]
variable_range = range(len(thisList))

for i in variable_range:
  number = thisList[i]
  print(number) #------ outputs 1 2 3 4 5


