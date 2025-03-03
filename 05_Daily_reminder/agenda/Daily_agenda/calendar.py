
#-----------------------------------------------------------------------------
# Name: calendar.py       Enhanced New File (enhancedNewFile.py)
# Purpose:   Ask the user to enter the current day of the week (e.g., "Monday", "Tuesday").
# 2. Store the day in a variable.
# 3. Use conditional statements to recommend an activity based on the day.
# Author:      Jayden
#
# Created:     28-Febuary-2025
# Updated:     28-Febuary-2025
#----------------------------------------------------------------

#Ask the user to enter the current day of the week (e.g., "Monday") and ttore the day in a variable.   The user input will be changed to lower case text.
dayOftheweek = input("What day of the week is it?: ").lower()

#once you respond the code will identify what day you chose and will give you a response.

if dayOftheweek == "monday":
    print("It's Monday, time to get ready for work!")
elif dayOftheweek == "tuesday":
    print("It's Tuesday, today's the day of your big project. Good luck!")
elif dayOftheweek == "wednesday":
    print("It's Wednesday: go to the gym.")
elif dayOftheweek == "thursday":
    print("It's Thursday: you're more than halfway through the week!")
elif dayOftheweek == "friday":
    print("It's Friday: Today is cheat day, eat whatever you want!")
else:
    print("Invalid day entered. Please enter a valid day of the week.")
