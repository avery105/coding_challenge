-----------------------------------------------------------------------------
# Name:grocery list       Enhanced New File (enhancedNewFile.py)
# Purpose:   . make a variable called fruit and add more groceries to the variable
# 3. Use conditional statements to print the grade based on the score
# Author:      Jayden

myName = input("What is your Name? ")

# Define the fruit list
myFruit = "apple juice, orange juice, pineapple juice"

# Greet the user and share the grocery list
print(f"Alright {myName}, I made a grocery list for us.")
print("It consists of: fruit.")

# Ask the user if they remember what "fruit" means
fruit_answer = input("Do you remember what I mean by fruit (yes/no): ").strip().lower()

if fruit_answer == "no":
    # Remind the user of what "fruit" means
    print(f"When I say fruit, I mean: {myFruit}.")
else:
    # Acknowledge that the user remembers
    print("Great! You remembered.")

# Ask the user if anything is missing from the grocery list
missing_items = input("Are we missing anything? (yes/no): ").strip().lower()

if missing_items == "yes":
    # Ask the user what items are missing
    additional_items = input("Oh, I almost forgot the milk! What else did I forget? ").strip()

    # Confirm missing items added
    print(f"Got it! Adding milk and {additional_items} to the list.")
else:
    # Confirm the list is complete
    print("Great! The list is complete.")
