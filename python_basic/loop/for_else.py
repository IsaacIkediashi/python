#------ else statement specifies a block of code to be executed when the loop is finished.

for i in range(6):
  print(i) #------ outputs 0 1 2 3 4 5 Finally finished!
else:
  print('Finally finished!')

#------ the else block will NOT be executed if the loop is stopped by a break statement

#------ break the loop when x is 3, and see what happens with the else block
for i in range(6):
  if i == 3:
    break
  print(i)
else:
  print('Finally finished!') #------ outputs 0 1 2 

#------ if the loop breaks, the else block is not executed