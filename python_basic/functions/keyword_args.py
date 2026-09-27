# You can also send arguments with the key = value syntax

#This way the order of the arguments does not matter

def my_function(child3,child2,child1):
  print('The youngest child is ' + child3)
my_function(child1 = 'Emil', child2 = 'Tobias', child3 = 'Linus') #------ outputs The youngest child is Linus


#note the phrase keyword arguments are often shortened to kwargs in python documentations.
