# The syntax

#newlist = [expression for item in iterable if condition == True]

fruits = ['apple','banana','cherry','kiwi','mango']
newlist = [x for x in fruits if 'a' in x]
print(newlist) #------ outputs
#['apple']
#['apple', 'banana']
#['apple', 'banana']
#['apple', 'banana']
#['apple', 'banana', 'mango']
#['apple', 'banana', 'mango']

# Condition

#The condition is like a filter that only accepts the items that evaluate to True

# Only accept items that are not 'apple':
newlist = [x for x in fruits if x != 'apple']
print(newlist) #------ outputs ['banana', 'cherry', 'kiwi', 'mango']       

# the condition < if x != 'apple' > will return True for all elements other than 'apple', making the new list 
#contain all fruits except 'apple'. 

#The condition is optional and can be omitted:

# With no if statement:

newlist = [x for x in fruits ]
print(newlist) #------ outputs ['apple','banana','cherry','kiwi','mango']

# Iterable

#The iterable can be any iterable object, like a list,tuple,set e.t.c.

# You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
print(newlist) #------ outputs [0,1,2,3,4,5,6,7,8,9] 

#Same example, but with a condition:

# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist) #------ outputs [0,1,2,3,4]

# Expression

# The expression is the current item in the iteration, but it is also the outcome, 
#which you can manipulate before it ends up like a list item in the new list:

# Set the values in the new list to uppercase:

newlist = [x.upper() for x in fruits] 

print(newlist) #------ outputs ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# You can set the outcome to whatever you like:

# Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits] 

print(newlist) #------ outputs ['hello', 'hello', 'hello', 'hello', 'hello']


# The expression can also contain conditions, not like a filter, but as a way to mamipulate the outcome:

# Return 'orange' instead of 'banana':

newlist = [x if x != 'banana' else 'orange' for x in fruits]

print(newlist) #------ outputs ['apple', 'orange', 'cherry', 'kiwi', 'mango']

#------ the expression in the example above says: 
# 'Return the item if it is not banana, if it is banana return orange'. 


