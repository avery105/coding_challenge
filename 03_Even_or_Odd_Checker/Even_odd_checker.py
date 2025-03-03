#-----------------------------------------------------------------------------
# Name: even or odd counter   Enhanced New File (enhancedNewFile.py)
# Purpose: 1. Ask the user to enter a number.
# 2. Store the number in a variable.
# 3. Use conditional statements to check if the number is even or odd.
#     - If the number is even (i.e., divisible by 2), print: `"The number is even."`
#     - If the number is odd, print: `"The number is odd."`
# Author:      Jayden
#
# Created:     28-Febuary-2025
# Updated:     28-Febuary-2025
#----------------------------------------------------------------





yourNumber = int(input("Enter a number: "))
if yourNumber % 2 == 0:  # Check if the number is divisible by 2
    print("Even")  # If so, print "Even"
else:  # If not, execute the "else" block
    print("Odd")  # Print "Odd"
