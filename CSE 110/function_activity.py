def display_regular():
 print(request_statement)
def display_upper():
 print(request_statement.upper())
def display_lower():
 print(request_statement.lower())

print("Welcome to the words and statement turn out game! ") 
print("\nGive me a sentence")
request_statement = input("What is your message? ")
display_regular()
display_upper()
display_lower()