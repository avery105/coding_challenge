#while True:
#myNumber= int(input("what number am I thinking of?:"))
import random
randint = random.randint(1, 10)
# if myNumber == randint:

#   correct = True
    #this is my attempt of making a random number generator.
while True:
    myNumber = int(input("What number am I thinking of (between 1 and 10)?: "))
    if myNumber == randint:
        print("Correct! You guessed the right number.")
        break  # Exit the loop when the user guesses correctly
    else:
        print("Wrong number. Try again!")
