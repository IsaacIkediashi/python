u = 1 #int
v = 2.0 #float
w = 1j #complex
#------ convert from float to int
a = int(v)

#------ convert from int to float
b = float(u)

#------ convert from int to complex
c = complex(u)

print(a) #------ outputs 2
print(b) #------ outputs 1.0
print(c) #------ outputs 1 +0j

#------ It tells python to treat values like a string or a number
song4 = '150'
song5 = 250.25

playlist = int(song4) + song5 
print(playlist) #------ outputs 400.25


#------ we can use it to convert our inputs into a number,float e.t.c.
favoriteSong = input('what is your favorite song: ')
durationTime = input('can you share the song duration time: ')
print(f'The artist who sang the song is Isaac and he sang it for {int(durationTime)} minutes') #------ outputs The artist who sang the song is Isaac and he sang it for 2 minutes

#------ we can write it like this to
favoriteSong = input('what is your favorite song: ')
durationTime = int(input('can you share the song duration time: '))
print(f'The artist who sang the song is Isaac and he sang it for {durationTime} minutes') #------ outputs The artist who sang the song is Isaac and he sang it for 2 minutes

#------ note any input variable we want to use provided by the user is always a string value i.e a string data type 
#------ input is a string data type
#------ that is why we use specifying data types for inputs, because we cannot concatenate a string with a number

#------ we also can not int() a string
variable = int('I love beans')
print(variable) #------ error

