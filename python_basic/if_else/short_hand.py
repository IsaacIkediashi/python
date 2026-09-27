#------ if you have one statement to execute, you can put it on the same line as the if-statement

#One line if statement
a = 70
b = 50

if a > b: print('a is greater than b') #------ outputs a is greater than b

#Short hand if-else statements

#One line if-else statement
a = 2
b = 330

print('A') if a > b else print('B') #------ outputs B, this technique is known as Ternary Operations, or Conditional Expressions

#------ you can also have multiple else statements on the same line

#One line if-else statement, with 3 conditions
a = 330
b = 330

print('A') if a > b else print('=') if a == b else print('B') #------ outputs =