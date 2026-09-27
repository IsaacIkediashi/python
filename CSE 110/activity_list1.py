clients = []  # empty list
# client = ["John" , "Mary"]  # stored in lists


clients.append("John")
clients.append("Mary")
new_client = input("New client name: ")
clients.append(new_client)
#print items in a list one at a time without the square brackets
for client in clients:
  print(client)


clients = []
new_client = ""
while new_client != "quit":
  new_client = input("New client name: ")
  clients.append(new_client)
  if new_client != "quit":
   for client in clients:
     print(f"{client}")
