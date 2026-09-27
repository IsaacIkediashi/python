i = 1
while i < 6:
  print(i)     #------ outputs 1 2 3 4 5
  i += 1


#------ Exit the loop when i is 3, we use the break statement

#------ break statement - we can stop the loop even if the while condition is True

i = 1
while i < 6:
  print(i)      #------ outputs 1 2 3
  if i == 3:
   break
  i += 1

#------ continue

#------ continue statement can stop the current iteration and continue with the next

i = 1
while i < 6:
  i += 1
  if i == 3:
    continue    #------ skips to the next line
  print(i)   #------ outputs  2 4 5 6 because it starts from 1


#------- be careful where you keep the increment value i += 1 e.t.c.

i = 1
while i < 6:
  print(i)      #------ outputs 1 2 3
  if i == 3:
   break
  i += 1


i = 1
while i < 6:
  print(i)     #------ outputs 1 2
  i += 1
  if i == 3:
   break
  

   