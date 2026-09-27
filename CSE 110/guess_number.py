import random

number = random.randint(1,100)



while True:
  user_guess = int(input("What is your guess? "))
  if user_guess < number:
   print ("Higher") 
   
  if user_guess > number:
   print ("Lower")  
   
  if user_guess == number:
   print ("You guessed it!")  
   break