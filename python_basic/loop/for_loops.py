#------ for loops do not stop until the every value in the collection has been counted or iterated e.g strings or a list


cities = ['New York City','London','Tokyo','Accra','Mexico City','Santiago']

for city in cities:
  print(city) #------ New York City London Tokyo Accra Mexico City Santiago 

#------ note city is the iterator variable the one which it's value gets changed as it loops through the list
# it's value changes not overwritten as it selects each value and what to do with it
# the specific block of code to be executed 

#print them by referring to their index numbers
fruits = ['apple','banana','cherry','orange','watermelon','mango','guava','tangerine']
for i in range(len(fruits)): 
 print(fruits[i]) #------ prints values in the list variable ruits with the index number 'i'

 #outputs apple banana cherry orange watermelon mango guava tangerine - fruits and i combined together
 #instead of printing 0 1 2 3 4 5 6 7, i can assign the i to the variable fruits with the fruits list.

 #because i am using the index and fruits variable.


 #fruits[0] is equal to apple, fruit[1] is equal to banana, fruit[2] is equal to cherry e.t.c.
 




  