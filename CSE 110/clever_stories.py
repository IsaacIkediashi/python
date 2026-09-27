# Getting the user's input for each required word
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb_01 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ")
verb_02 = input("Enter a verb: ")
verb_03 = input("Enter a verb: ") 

# Adding more words to the story
verb_04 = input("Enter a verb: ")
verb_05 = input("Enter a verb: ")
verb_06 = input("Enter a verb: ")

# Making sure the exclamation starts with a capital letter
story = f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb_01} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all I could think to do was to {verb_02} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_03} right in front of my family. But then i {verb_04} into my {verb_05} and {verb_06} off."

# Print the story to get the result
print("\n\nHere's your story:\n")
print(story)
