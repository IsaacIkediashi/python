#------ You can specify the range of indexes by specifying where to start and where to end the range.

#------ When specifying a range, the return value will be a new list with the specified items


#Return the third,fourth and fifth item:
thisList = ['apple', 'banana', 'cherry','orange','kiwi','melon','mango']
print(thisList[2:5]) #------ outputs ['cherry','orange','kiwi',] 

#note it does not return the item in the fifth position


# This example returns the items from the beginning to, but NOT including 'kiwi' from index 0 to 4 
thisList = ['apple','banana','cherry','orange','kiwi','melon','mango']
print(thisList[:4]) #------ outputs ['apple','banana','cherry','orange']


# This example returns the items from 'cherry' to the end
thisList = ['apple','banana','cherry','orange','kiwi','melon','mango']
print(thisList[2:]) #------ outputs ['cherry','orange','kiwi','melon','mango']

#it will return the items from index 2 to the end

# Range of negative indexes

#specify negative indexes if you want to start the search from the end of the list:
 
thisList = ['apple','banana','cherry','orange','kiwi','melon','mango']
print(thisList[-4:-1]) #------ outputs ['orange','kiwi','melon']

#note negative indexing means starting from the end of the list, 
# it returns the items from index -4 included to index -1 excluded, remember that the last item has the index -1


