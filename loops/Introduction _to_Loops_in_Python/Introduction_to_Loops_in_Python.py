#**Example:** Print numbers from 1 to 5 using a `for` loop.
#```python
#for num in range(1, 6):
#print(num)
#-----------------------------------------------------------------------------
# Name: student grading       Enhanced New File (enhancedNewFile.py)
# Purpose:   . .
# 2. Store the score in a variable.
# 3. Use conditional statements to print the grade based on the score
# Author:    Jayden


counter = 0
while counter < 7:
    print(counter)
    counter += 1

user_exit = "no"  # Changed the variable name to avoid using the reserved word 'exit'
while user_exit != "yes":
    user_exit = input("Do you really want to exit? (yes/no)").lower()