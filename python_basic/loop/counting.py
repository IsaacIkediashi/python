#------ counting using for loop
numbers = [1,2,3,4,5]

for number in numbers:
  print(number) #------ outputs 1 2 3 4 5

#------ if we needed a 100 or 1000 or a 1000,000 that would be a long list i.e [1,2,3,4,5...,1000 e.t.c.] 

# we will use a range() function
for number in range(1,10,1):
  print(number) #----- outputs 1 2 3 4 5 6 7 8 9

#------ for loop using range()
for number in range(1,11,2):
  print(number) #------ outputs 1 3 5 7 9 

