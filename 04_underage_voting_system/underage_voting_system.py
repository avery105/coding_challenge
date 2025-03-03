#-----------------------------------------------------------------------------
# Name: underage voting system      Enhanced New File (enhancedNewFile.py)
# Purpose:  Ask the user to enter their age.
# 2. Store the age in a variable.
# 3. Use conditional statements to check if the person is eligible to vote.
#     - If the age is 18 or older, print: `"You are eligible to vote!"`
#     - If the age is under 18, print: `"Sorry, you are not eligible to vote yet
# Author:      Jayden
#
# Created:     28-Febuary-2025
# Updated:     28-Febuary-2025
#----------------------------------------------------------------




print("Welcome to the Underage Voting System!")
yourName = input("What is your name? : ")
print("hello yourName do you want to vote?")
vote = input("yes or no : ")
if vote == "yes":
    print("yourName has voted")
else:
  print("has not voted","yourName")
yourAge = int(input("What is your age and don't lie please : "))
if yourAge <=18: print("too young")

if yourAge >=18:print("say alright then")