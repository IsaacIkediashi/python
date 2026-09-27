mylist = ['apple','banana','cherry']

#------ lists are used to store multiple items in a variable

thisList = ['apple','banana','cherry']
print(thisList) #------ outputs ['apple', 'banana', 'cherry']

#------ indexes are used in lists 

#first item has index 0
#second item has index 1


#------ list has items that can be of the same value.
thisList = ['apple', 'banana', 'cherry','apple', 'banana', 'cherry']
print(thisList) #------ outputs ['apple', 'banana', 'cherry','apple', 'banana', 'cherry']


#list length to determine how many items a list has i.e length of the list use the len() function
thisList = ['apple', 'banana', 'cherry']
print((thisList)) #------ outputs 3

#list items can be of any Data type

#string, int, boolean data types
list1 = ['apple', 'banana', 'cherry']
list2 = [1,5,7,9,3]
list3 = [True,False,False]

print(list1) #------ outputs ['apple', 'banana', 'cherry']
print(list2) #------ outputs [1,5,7,9,3]
print(list3) #------ outputs [True,False,False]

#string, int, and boolean values
list1 = ['abc',34,True,40,'male',False]
print(list1) = ['abc',34,True,40,'male',False]

#type()

#------ python defines a list as an object with the data type 'list'
#<class 'list'>

mylist = ['apple', 'banana', 'cherry']
print(type(mylist)) #------ outputs <class 'list'>

#The list() constructor: used to specify or construct a new list or make a list

thisList = list(('apple', 'banana', 'cherry')) #------ note the double round brackets
print(thisList) #------ outputs ['apple', 'banana', 'cherry']


# list items are indexed and you can access them by referring to their index number
#------ note the first item has index 0


#print the second item of the list
thisList = ['apple', 'banana', 'cherry']
print(thisList[1])


# Negative Indexing
# it means start from the end -1 refers to the last item, -2 refers to the second last item e.t.c.

#print the last item of the list
thisList = ['apple', 'banana', 'cherry']
print(thisList[-1]) #------ outputs cherry


