#**Example:** Print numbers from 1 to 5 using a `for` loop.
#```python
#for num in range(1, 6):
#print(num)

counter = 0
while counter < 7:
    print(counter)
    counter += 1

exit = "no"
while exit != "yes":
    exit = input("Do you really want to exit? (yes/no) ").lower()
