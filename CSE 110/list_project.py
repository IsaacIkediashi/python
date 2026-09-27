user_numbers = []
total = 0
largest = 0
print("Enter a list of numbers, type 0 when finished.")

while True:
 number = float(input("Enter a number: "))
 user_numbers.append(number)
 #print items in a list one at a time without the square brackets
 if number == 0:
  break 
 
for num in user_numbers:
 total += num
 if num > largest:  # Check if the current number is greater than the largest found so far
        largest = num   # Update largest if the current number is greater

   
if len(user_numbers) > 0:
    average = total / len(user_numbers)
else:
    average = 0
 

print(f"The sum is: {total}")
print(f"The average is: {average:.2f}")
print(f"The largest number is: {largest}")
