cart_list_names = []
cart_list_prices = []
cart_list_quantities = []

total = 0

print("Welcome to the Enhanced Shopping Cart Program!")
print("You can add items, view your cart, remove items, update quantities, compute the total, or quit.")

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Update item quantity")
    print("5. Compute total")
    print("6. Clear cart")
    print("7. Quit")

    user_action = int(input("Please enter an action: "))
    
    if user_action == 1:
        item_name = input("What item would you like to add? ")
        item_price = float(input(f"What is the price of '{item_name}'? "))
        item_quantity = int(input(f"How many '{item_name}' would you like to add? "))
        cart_list_names.append(item_name)
        cart_list_prices.append(item_price)
        cart_list_quantities.append(item_quantity)
        print(f"'{item_name}' (x{item_quantity}) has been added to the cart.")
    elif user_action == 2:  
        if not cart_list_names:
            print("Your cart is empty.")
        else:
            print("The contents of the shopping cart are: ")
            for i in range(len(cart_list_names)):
                print(f"{i + 1}. {cart_list_names[i]} (x{cart_list_quantities[i]}) - ${cart_list_prices[i]:.2f} each")
    elif user_action == 3:
        if not cart_list_names:
            print("Your cart is empty. No items to remove.")
        else:
            print("The contents of the shopping cart are: ")
            for i in range(len(cart_list_names)):
                print(f"{i + 1}. {cart_list_names[i]} (x{cart_list_quantities[i]}) - ${cart_list_prices[i]:.2f} each")
            
            pop_out = int(input("Which item would you like to remove? ")) - 1
            if 0 <= pop_out < len(cart_list_names):
                cart_list_names.pop(pop_out)
                cart_list_prices.pop(pop_out)
                cart_list_quantities.pop(pop_out)
                print("Item removed.")
            else:
                print("Sorry, that is not a valid item number.")
    elif user_action == 4:
        if not cart_list_names:
            print("Your cart is empty. No items to update.")
        else:
            print("The contents of the shopping cart are: ")
            for i in range(len(cart_list_names)):
                print(f"{i + 1}. {cart_list_names[i]} ({cart_list_quantities[i]}) - ${cart_list_prices[i]:.2f} each")
            
            update_item = int(input("Which item would you like to update? ")) - 1
            if 0 <= update_item < len(cart_list_names):
                new_quantity = int(input(f"Enter the new quantity for '{cart_list_names[update_item]}': "))
                cart_list_quantities[update_item] = new_quantity
                print(f"Quantity for '{cart_list_names[update_item]}' updated to {new_quantity}.")
            else:
                print("Sorry, that is not a valid item number.")
    elif user_action == 5:
        total = 0
        for i in range(len(cart_list_prices)): 
            total += cart_list_prices[i] * cart_list_quantities[i]
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    elif user_action == 6:
        cart_list_names.clear()
        cart_list_prices.clear()
        cart_list_quantities.clear()
        print("Your cart has been cleared.")
    elif user_action == 7:
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice, please choose a valid option.")
