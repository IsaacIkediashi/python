# 1 Thes 5:16
scripture = 'Rejoice evermore.'

for letter in scripture:
  print(letter) #------ outputs R e j o i c e  e v e r m o r e .

#------ you can get a letter by it's index 

# 1 Thes 5:16
scripture = 'Rejoice evermore.' 
letter = scripture[2]
print(letter) #------ outputs j index 2 is the third letter

# 1 Thes 5:16
scripture = 'Rejoice evermore.'

for letter in scripture[1]:
  print(letter) #------ outputs e

for i in range(17):
  print(i) #------ outputs 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 

#------ loop through a string
# 1 Thes 5:16
scripture = 'Rejoice evermore.'

for i in range(17):
  letter = scripture[i] #------ using scripture[0] it gets the letter with the position 0 which in this case is R
  print(letter) #------ outputs R e j o i c e  e v e r m o r e .


#OR
 # 1 Thes 5:16
scripture = 'Rejoice evermore.'

scripture_length = len(scripture) #------ length of the string

for i in range(scripture_length):
  letter = scripture[i]
  print(letter) #------ outputs R e j o i c e  e v e r m o r e .

#------ note looping through a string with range gets letters with their positions and prints it
