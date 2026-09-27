# Target word to guess
target_word = "HELLO"

# Prompt user for their guess
guess = input("Enter your guess: ").upper()

# Initialize result variable
result = ""

# Check each letter in the guess
for i in range(len(target_word)):
        if guess[i] == target_word[i]:
            result += guess[i]  # Correct letter and position
        elif guess[i] in target_word:
            result += guess[i].lower()  # Correct letter but wrong position
        else:
            result += guess[i]  # Incorrect letter


# Display the result
print("Result:", result)
