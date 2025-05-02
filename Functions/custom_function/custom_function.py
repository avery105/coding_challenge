#-----------------------------------------------------------------------------
# Name:        Functions (functions_ex4.py)
# Purpose:     to greet three people at once
#
# Author:     Jayden
# Created:     1-May-2025
# Updated:     2-May-2025
#-----------------------------------------------------------------------------

def greet(name, greeting='Hello'):
    '''A function that returns a personalized greeting.'''
    return f'{greeting}, {name}!'

# Example usage
#print(greet('John'))                  # Uses default greeting
#print(greet('Jim', 'Hi'))             # Custom greeting
#print(greet('Josiah', 'Hey'))         # Another custom greeting

# If you want to store people with greetings, use a dictionary
person={
    'person1': ('John', 'Hello'),
    'person2': ('Jim', 'Hi'),
    'person3': ('Josiah', 'Hey')
}
print(person)