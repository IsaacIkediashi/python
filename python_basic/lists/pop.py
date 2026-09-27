# The pop() method removes the specified index

#Remove the second item:

thisList = ['apple','banana','cherry']
thisList.pop(1)

print(thisList) #------ outputs ['apple', 'cherry']

#if you do not specify the index, the pop() method removes the last item.

thisList = ['apple','banana','cherry']
thisList.pop()

print(thisList) #------ outputs ['apple', 'banana']

