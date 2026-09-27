# You can loop through the list items by using a while loop

#use the len() function to determine the length of the list, then start at 0 to initialise the while loop
# and loop your way through the list items by referring to their indexes.

# Print all items, using a while loop to go through all the index numbers:

thisList = ['apple','banana','cherry']
i = 0
while i < range(len(thisList)):
  print(thisList[i]) #------ outputs apple banana cherry
  i += 1


  