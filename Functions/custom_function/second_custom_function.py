#-----------------------------------------------------------------------------
# Name:        Functions (functions_ex4.py)
# Purpose:     To say three teachers name and say what courses they teach students.
#
# Author:     Jayden
# Created:     1-May-2025
# Updated:     2-May-2025
#-----------------------------------------------------------------------------
def greet(name,courses):
    '''A function that returns a personalized greeting.'''
    return f'{courses}, {name}!'
person={
    'person1': ('Ms.Hill', 'English'),
    'person2': ('Mr.Daniels', 'Civics/Careers'),
    'person3': ('Mr.Dinowski', 'Computer Science')
}
print(person)