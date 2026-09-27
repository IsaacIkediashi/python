# Python Read Files

# Python File Open - Open a file on the server

# Assume we have the following file located in the same folder as python:

#  demofile.txt

# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# to open this file we use the built-in open() function. The open() function returns a file object, which has a
# read() method for reading the content of the file.

f = open('demofile.txt', 'r')
print(f.read()) #------ outputs Hello! Welcome to demofile.txt
                        #------ The file is for testing purposes.
                        #------ Good Luck!

#If the file is located in a different location, you will have to specify the file path, like this:

# Open a file on a different location:
f = open('C:\\myfiles\welcome.txt','r')
print(f.read()) #------ outputs Welcome to this text file!             
                        #------ This file is located in a folder named 'myfiles' on the D drive.
                        #------ Good Luck!

# Read Only Parts Of The File

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# Return the first 5 characters of the file:
f = open('demofile.txt', 'r')
print(f.read(5)) #------ outputs Hello


# Read Lines

# You can return one line by using the readline() method:
f = open('demofile.txt', 'r')
print(f.readline()) #------ outputs Hello! Welcome to demofile.txt

# By calling readline() two times, you can read the two firstlines:

# Read two lines of the code:
f = open('demofile.txt','r')
print(f.readline())
print(f.readline()) #------ outputs Hello! Welcome to demofile.txt
                            #------ The file is for testing purposes.


#By looping through the lines of the file, you can read the whole file line by line:

# loop  through the file line by line:

f = open('demofile.txt','r')
for i in f:
  print(i) #------ outputs Hello! Welcome to demofile.txt
                    #------ The file is for testing purposes.
                    #------ Good Luck!

#The split() function works for text files automatically they are strings, so it will read each line as a string

#python reads line by line in a text file, then it takes each line as a single string or items in a file we can
#turn or split each line into a list, with the words in the string as the items in the list.