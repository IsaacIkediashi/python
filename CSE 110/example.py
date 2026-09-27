age = int(input("How old are you? "))
age_next_year = age + 1
print(f"On your next birthday, you will be {age_next_year}.")
print()  # This prints a blank line
#I am asking the user for the number of egg cartons they have
egg_cartons = int(input("How many egg cartons do you have? "))
 #Using the assumption that each carton holds 12 eggs
eggs_in_total = egg_cartons * 12
print(f"You have {eggs_in_total} eggs")
# In the next example, to create a blank line I included \n at the beginning of the string
cookies = int(input("\nHow many cookies do you have? "))
people = int(input("How many people are there? "))

cookies_per_person = cookies / people

print(f"Each person may have {cookies_per_person} cookies")

