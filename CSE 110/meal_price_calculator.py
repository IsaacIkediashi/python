# Getting the values for the total price of a meal
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
tip_percentage = float(input("What is the tip percentage? ")) / 100
drinks_price = float(input("What is the price of drinks? "))
appetizers_price = float(input("What is the price of appetizers? "))

# Calculate total cost
total_cost = adult_meal_price + drinks_price + appetizers_price + (adult_meal_price * tip_percentage)

number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

# Displaying the meal's subtotal
meals_subtotal = (child_meal_price * number_of_children) + (total_cost * number_of_adults)

print(f"\n\nSubtotal: ${meals_subtotal:.2f}\n\n")

#----------------------------------------------------------------
sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (meals_subtotal * sales_tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")

#--------------------------------------------------------------------------
total_amount = meals_subtotal + sales_tax 
print(f"Total: ${total_amount:.2f}\n\n")

#-----------------------------------------------------------------
# Asking for the payment amount
payment_amount = float(input("What is the payment amount? "))
change_amount = payment_amount - total_amount
# I am displaying the change amount
# Display the change amount

print(f"Change: ${change_amount:.2f}.")
