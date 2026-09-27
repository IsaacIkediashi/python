name = 'Sister Hansen'

print(f'{name}') #------ outputs 'Sister Hansen'

# strip() - removes whitespaces around strings 
# from the start and end of a string, it is also known as leaving and trailing whitespace.

name = '  Sister Hansen  '

print(f'{name}') #------ '  Sister Hansen  '

# You need to store it in a variable:
name = '  Sister Hansen  '
name.strip()
print(f'{name}') #------ '  Sister Hansen  '

name = '  Sister Hansen  '
name_stripped = name.strip()
print(f'{name}') #------ '  Sister Hansen  '
print(f'{name_stripped}') #------ 'Sister Hansen'

#OR

name = 'Sister Hansen'

print(f'   {name}   ') #------ '  Sister Hansen  '

# With strip() method:
name = 'Sister Hansen'
name_stripped = name.strip()
print(f'   {name}   ') #------ '  Sister Hansen  '
print(f'{name_stripped}') #------ 'Sister Hansen'

