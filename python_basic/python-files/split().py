# split() - To convery words treated as a single string into a different format that is into a list.

colors = 'red green blue orange yellow'
color_list = colors.split()
print(color_list) #------ outputs ['red', 'green', 'blue', 'orange', 'yellow']

# remember: colors = 'red green blue orange yellow'

print(color_list[1]) #------ outputs green

# scope: It will look for whitespace to split the string into pieces.

# Putting Commas

# We can tell the split method to look for commas instead of whitespaces:

colors = 'red, green, blue, orange yellow'
color_list = colors.split(',')
print(color_list) #------ outputs ['red', 'green', 'blue', 'orange yellow'] # note orange and yellow are together

# You need to know if your line is seperated by comma first

# In a file reading case. before using the comma instead of whitespace you want to read line by line.

# When you read from a file, it reads as a string, use float() or int() sometimes i.e when getting a value from a file.
