# My adventure game has been improved  with my own additional levels, hidden choices, and trick questions to provide a wonderful experience for my friends. 

print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")
user_choice = input("Type MATCH or FLASHLIGHT: ").lower()

if user_choice == "match":
    print("You pick up the match and strike it. The forest is briefly illuminated, and you see a grizzly bear! Do you want to RUN or HIDE?")
    choice = input("Type RUN or HIDE: ").lower()

    if choice == "run":
        print("You run as fast as you can and barely escape the bear! You reach a river. Do you want to SWIM across or BUILD a raft?")
        river_choice = input("Type SWIM or BUILD: ").lower()
        if river_choice == "swim":
            print("You swim across and make it safely to the other side!")
        elif river_choice == "build":
            print("You build a raft and float across the river safely.")
        else:
            print("Invalid choice. Please type SWIM or BUILD.")
    elif choice == "hide":
        print("You hide behind a tree and the bear walks past you. You survive!")
    else:
        print("Invalid choice. Please type RUN or HIDE.")

elif user_choice == "flashlight":
    print("You pick up the flashlight and turn it on. You see the path ahead, but you hear a noise nearby. Do you want to FOLLOW the path or LOOK in the trees?")
    choice = input("Type FOLLOW or LOOK: ").lower()

    if choice == "follow":
        print("You follow the path and safely reach a clearing. You find a mysterious object. Do you want to TAKE it or IGNORE it?")
        object_choice = input("Type TAKE or IGNORE: ").lower()
        if object_choice == "take":
            print("You take the object and discover it's a magical amulet!")
        elif object_choice == "ignore":
            print("You ignore the object and continue on your way.")
        else:
            print("Invalid choice. Please type TAKE or IGNORE.")
    elif choice == "look":
        print("You find a hidden cave with treasure inside!")
    else:
        print("Invalid choice. Please type FOLLOW or LOOK.")

else:
    print("Invalid choice. Please type MATCH or FLASHLIGHT.")
