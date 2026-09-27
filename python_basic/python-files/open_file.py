# The key function for working with files in python is the open() function.

# The open() function takes two parameters: file name and mode

# To open a file for reading it is enough to specify the name of the file:
f = open('demofile.txt')

# the code above is the same as:
f = open('demofile.txt', 'rt')

# because 'r' for read, and 't' for text are the default values, you do not need to specify them.

# note make sure the file exists, or else you will get an error.