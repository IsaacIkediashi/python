# To append elements from another list to the current list, use the extend() method

#add the elements of tropical to thisList:

thisList = ['apple','banana','cherry']
tropical = ['mango','pineapple','papaya']

thisList.extend(tropical)
print(thisList) #------ outputs ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya'] the elements will be 
#added to the end of the list.