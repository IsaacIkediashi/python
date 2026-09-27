#Change Item Value
# To change the value of a specific item, refer to the index number

#change the second item
thisList = ['apple','banana','cherry']
thisList[1] = 'blackcurrant'

print(thisList) #------ ['apple', 'blackcurrant', 'cherry']


#Change a range of item Values
# To change the value of items within a specific range

#change the values 'banana' and 'cherry' with the values 'blackcurrant' and 'watermelon'
thisList = ['apple','banana','cherry','orange','kiwi','mango']
thisList[1:3] = ['blackcurrant','Watermelon']

print(thisList) #------ outputs ['apple','blackcurrant','watermelon','orange','kiwi','mango']

#change the second value by replacing it with two new values
thisList = ['apple','banana','cherry']
thisList[1:2] = ['blackcurrant','Watermelon']

print(thisList) #------ outputs ['apple', 'blackcurrant', 'watermelon', 'cherry]
#note if you insert more values than you replace, the new items will be inserted in place of that item, the remaining will move accordingly

#change the second and third value by replacing it with one value
thisList = ['apple','banana','cherry']
thisList[1:3] = ['Watermelon']
print(thisList) #------ ['apple','watermelon']


