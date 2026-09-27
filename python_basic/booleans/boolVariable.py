#------ booleans returns true or false if the condition is right or wrong
#------ we can save boolean values in variables that return true or false

men = int(input('How many men are there? '))
women = int(input('How many women are there? '))

total = men + women

#------ if total is greater than or equals to 7 it returns true, therefore has_enough_players variable is True
has_enough_players = total >= 7 
has_enough_women = women >= 4 #------ if total is greater than or equals to 4 it returns true

if has_enough_players and has_enough_women:
  print('You can play!') #------ outputs You can play!
else:
  print('You cannot play a legal game.')