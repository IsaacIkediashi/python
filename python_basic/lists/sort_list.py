# List objects have a sort method that will sort the list alphanumerically,ascending,by default:

# Sort the lists Alphanumerically:
thisList = ['orange','mango','kiwi','pineapple','banana']
thisList.sort()

print(thisList) #------ outputs ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort the lists numerically:
thisList = [100,50,65,82,23]
thisList.sort()

print(thisList) #------ outputs [23, 50, 65, 82, 100]

# Sort descending

#To sort descending, use the keyword argument (reverse = True):

# Sort the list descending:
thisList = ['orange','mango','kiwi','pineapple','banana']
thisList.sort(reverse = True)

print(thisList) #------ outputs ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# Sort the list descending:
thisList = [100,50,65,82,23]
thisList.sort(reverse = True)

print(thisList) #------ outputs [100, 82, 65, 50, 23]


# Customize Sort Function

# You can also customize your own function by using the keyword argument (key = function). The function will return a number 
# that wil be used to sort the list (the lowest number)

# Sort the listed based on how close the number is to 50:

def myfunc(n):
  return abs(n-50)
thisList = [100,50,65,82,23]
thisList.sort(key = myfunc)
print(thisList) #------ outputs [50,65,82,100]

# Case - Insensitive sort

# By default the sort() method is case sensitive, resulting in all capital letters 
#being sorted before lower case letters

# Case sensitive sorting can give an unexpected result:

thisList = ['banana', 'orange', 'kiwi', 'cherry']
thisList.sort()

print(thisList) #------ outputs ['kiwi', 'orange', 'banana', 'cherry']

#Luckily we can use built-in functions as key functions when sorting a list, so if you want a case-insensitive
#sort function, use str.lower as a key function:

# Perform a case-insensitive sort of the list:
thisList = ['banana', 'Orange', 'Kiwi', 'cherry']
thisList.sort(key = str.lower)

print(thisList) #------ outputs ['banana', , 'cherry', 'orange', 'kiwi']

#Reverse Order

#what if you want to reverse the order of a list, regardless of the alphabet?
#answer: The reverse() nethod reverses the current sorting order of the elements.


# Reverse the order of the list items:
thisList = ['banana', 'orange', 'kiwi', 'cherry']
thisList.reverse()

print(thisList) #------ outputs [ 'cherry', 'kiwi', 'orange', 'banana']

