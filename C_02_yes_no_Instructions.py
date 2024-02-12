print("🎲🎲 Roll it 13 🎲🎲")


# loop for testing purposes

while True:
    want_instructions = input("Would you like to read the instructions").lower()

# check users enter yes (y) or no (n)
    if want_instructions == "yes" or want_instructions == "y":
        print("You chose yes")
    elif want_instructions == "no" or want_instructions == "n":
        print("you chose no")
    else:
        print("you did not choose a valid response")
