#------ A string is a combination of characters i.e characters of text 
#------ strings are surrounded by quotation marks i.e a piece of text data


#------ converting strings way of being displayed using string methods

#------ converting string to upper case
name = 'Isaac'
print(name.upper()) #------ outputs ISAAC

#------ converting string to lower case
name = 'Isaac'
print(name.lower()) #------ outputs isaac

#------ Capitalizes the first word, starts every sentence with a capital letter
name = 'isaac is a good boy'
print(name.capitalize()) #------ outputs Isaac is a good boy

#------ making every word a title
name = 'isaac is a good boy'
print(name.title()) #------ outputs Isaac Is A Good Boy

#------ counts the number of a word in a sentence
name = 'isaac is a good boy'
print(name.count('i')) #------ outputs 2

#------ we can use multiple string methods
name = 'Isaac is a good boy, it is true'
print(name.lower().count('i')) #------ outputs 4,
#------ note: it converts to lowercase then counts the number of 'i' in the sentence not 'I'

name = 'Isaac is a good boy, it is true'
print(name.lower().count('I')) # outputs 0, no uppercase letter 'I' in the converted sentence to lowercase