#------ generating a random number
import random

# Generate and print a random number between 1 and 6 (inclusive)
random_number = random.randint(1, 6)
print(f'Random number between 1 and 6: {random_number}')

# Confirmation message
print("Random number generation script executed successfully.")

if random_number == 3:
  print('I said it')