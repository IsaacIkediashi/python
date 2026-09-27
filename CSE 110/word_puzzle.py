print("Welcome to the word guessing game")
secret = "great"
attempts = 0
hint = "_ _ _ _ _"

 
print(f"Your hint is: {hint}")




#So that the print shows in the program line 7 and enters the loop to ask once what is your guess instead of declaring 
#it before the loop and results in the program asking twice so i set the while loop to evaluate to true and then 
#asks the user for is input then use my if -statements and for loop to fulfill requirements
while True:
    user_input = input("What is your guess? ").lower()
    hint = " " 


    for i in range(len(secret)):
            if  user_input[i] == secret[i]:
                hint += user_input[i].capitalize() 
            elif user_input[i] in secret:
                hint += user_input[i].lower()

            else:
                    hint += "_ "
    #prints hint (variable) after loop is over i.e the result, If aligned or indented with the loop it will loop the result by
    #showing prints one by one instead of once and for all.
    print(f"Your hint is:{hint}")

            

    if len(user_input) != len(secret): 

        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    attempts += 1
    if user_input == secret and attempts == 1:
        print(f"Bravo! You guessed it!. it took you only {attempts} guess")
        break
    if user_input == secret:
        print(f"Congratulations! You guessed it!. it took you only {attempts} guesses")
        break
    else:
        print("Your guess was not correct.")
