# you can not copy a list simply by typing list 2 = list 1, because list 2 will only be a reference to list 1

#changes made in list 1 will automatically also be made in list 2

#we can copy a list using the copy() method

# Make a copy of a list with the copy() method:

thisList =  ['apple','banana','cherry']
myList = thisList.copy()
print(myList) #------ outputs  ['apple','banana','cherry']

