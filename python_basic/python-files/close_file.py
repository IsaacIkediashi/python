#It is a good practice to always close the file when you are done with it:

# Close the file when you are finished with it:

f = open('demofile.txt','r')
print(f.readline())
f.close() #------- outputs Hello! Welcome to demofile.txt


# note you should always close your file, in some cases due to buffering, changes made to a file
#  may not show until you close the file.


