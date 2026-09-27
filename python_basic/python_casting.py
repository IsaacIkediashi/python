#------ specifying a variable type i.e specifying a type on to a variable is known as casting

#------ casting is done with the following functions known as constructor functions

#int() removes decimals from a float number, constructs an integer number from a string, 
# providing the string represents a whole number
#float() constructs an integer number from a string, providing the string represents a float or an integer
#string() constructs a string from a wide variety of data types including strings, integer literals and float literals

x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int('3') # z will be 3

w = float(1) # w will be 1.0
x = float(2.8) # x will be 2.8
y = float('3') # y will be 3.0
z = float('4.2') # z will be 4.2

x = str('s1') # x will be 's1'
y = str(2) # y will be '2'
z = str(3.0) # z will be '3.0'

print(x) #------ outputs s1
print(y) #------ outputs 2
print(z) #------ outputs 3.0

#int() is also used to specify an integer is an integer
#float() is also used to specify a float is a float
#string() is also used to specify a string is a string

x = int(1)
y = float(3.0)
z = str('Isaac')

print(x) #------ outputs 1
print(y) #------ outputs 3.0
print(z) #------ outputs Isaac

song1 = 162
song2 = 175
song3 = int(input('What is the length of the song? '))

playlist = song1 + song2 + song3

print(f'The playlist has {playlist} seconds') #------ outputs The playlist has 372.67 seconds
