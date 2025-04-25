#set4 =10,20,30,40,50
#copied_set4 = set4
#print(copied_set4)

data = {10, 20, 30, 40, 50}
print("Original Set:", data)

# Copy the set to data_copy
data_copy = data.copy()
print("Copied Set:", data_copy)

# Use .pop() to remove a random element and print the set
removed_element = data.pop()  # .pop() removes a random element
print("Set after pop (removed element):", data)
print("Removed Element:", removed_element)

# Use .clear() to empty the set and print it
data.clear()
print("Set after clear:", data)



