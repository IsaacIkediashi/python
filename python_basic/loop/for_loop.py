#------ for loop is for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

#------ for loop does not require an indexing variable to set before hand like while loop - i = 1 e.t.c. to start loops.


#------ loops through strings list tuples dictionary or a set

#------ loop through a string
for word in 'banana':
  print(word) #------ outputs b a n a n a

#------ print each fruit in a fruit list
fruits = ['apple','banana','cherry']
for i in fruits: 
 print(i) #------ outputs apple banana cherry

#------ using a break statement can stop the loop before it has looped through all the items.
fruits = ['apple','banana','cherry']
for i in fruits: 
 print(i) #------ outputs apple banana 
 if i == 'banana':
  break
 
 #------ exit the loop when i is 'banana' but this time the break comes before the print
fruits = ['apple','banana','cherry']
for i in fruits: 
 if i == 'banana':
  break
 print(i) #------ outputs apple 

#------ using a continue statement we can stop the current iteration of the loop and continue with the next same as
# skips to the next line

fruits = ['apple','banana','cherry']
for i in fruits: 
 if i == 'banana':
  continue
 print(i) #------ outputs apple cherry
 
