#------ a nested loop is a loop inside a loop 
#------ The 'The inner loop' will be executed one time for each iteration of the outer loop.

#------ print each adjective for every fruit:

adj = ['red','big','tasty']
fruits = ['apple','banana','cherry']

#------ for nested loops once the outer loop is run once the inner loop runs until the end or loops until the end
for i in adj:
  for j in fruits:
    print(i,j) #------ red apple red banana red cherry big apple big banana big cherry tasty apple tasty banana tasty cherry

for i in adj:  #------ runs loop once as red big and tasty
  for j in fruits:
    print(j) #------ outputs for red: apple banana cherry | for big: apple banana cherry | for tasty: apple banana cherry