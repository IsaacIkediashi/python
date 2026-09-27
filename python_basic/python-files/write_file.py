# To write to an existing file, you must add a parameter to the open() function:

# ['a'] - Append - will append to the end of the file
# ['w'] - Write - will overwrite any existing content

# Open the file 'demofile2.txt' and append content to the file:
f = open('demofile.txt','a')
f.write('Now the file has more content!')
f.close

# open and read the file after the appending:
f = open('demofile2.txt','r')
print(f.read()) #------ outputs Hello! Welcome to demofile.txt
                        #------ The file is for testing purposes.
                        #------ Good Luck! Now the file has more content!

# Open the file 'demofile3.txt' and overwrite the content:
f = open('demofile3.txt','w')
f.write('Woops! I have deleted the content!')
f.close()

# open and read the file after the appending:
f = open('demofile3.txt', 'r')
print(f.read()) #------ outputs Woops! I have deleted the content!

# note the 'w' method will overwrite the entire file.


#'w' is input
#'r' is output 

#that is why we need the output to read the input - r to print out w.