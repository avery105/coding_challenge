
myNumber1 = int(input ("pick a first number it doesn't matter what number it is:"))
myNumber2 = int(input ("pick a second number it doesn't matter what number it is:"))
tuple = (myNumber1, myNumber2)
print (tuple)
tuple = (tuple[1], tuple[0])
print (tuple)