x = 1 #int
y = 2.8 #float
z = 1j #complex

print(type(x)) #------ outputs <class 'int'>
print(type(y)) #------ outputs <class 'float'>
print(type(z)) #------ outputs <class 'complex'>

# int is a whole number, positive or negative without decimals
x = 1
y =36776276626726736388787373
z = -72683878873

print(type(x)) #------ outputs <class 'int'>
print(type(y)) #------ outputs <class 'int'>
print(type(z)) #------ outputs <class 'int'>

# float is a number positive or negative containing one or more decimals
x = 1.10
y = 1.0
z = -35.59

print(type(x)) #------ outputs <class 'float'>
print(type(y)) #------ outputs <class 'float'>
print(type(z)) #------ outputs <class 'float'>
# float can also be scientific numbers with an 'e' to indicate the power of 10

x = 35e3
y = 12E4
z = -87.7e100


print(type(x)) #------ outputs <class 'float'>
print(type(y)) #------ outputs <class 'float'>
print(type(z)) #------ outputs <class 'float'>

# complex is a number written with 'j' as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(type(x)) #------ outputs <class 'complex'>
print(type(y)) #------ outputs <class 'complex'>
print(type(z)) #------ outputs <class 'complex'>


