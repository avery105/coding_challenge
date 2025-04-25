#set1=(1,2,3,4)
#set2=(3,4,5,6)

#print(set1)

#union_set=(set1set2))
#print(union_set)



#print(set1)

#this is set1 and set2 unionized together

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}  # Use sets, not tuples

print("set1:", set1)

# This is set1 and set2 unionized together
union_set = set1 | set2
#printing the unionized set
print("union_set:", union_set)

set1.intersection_update(union_set)

print("Updated set1 with intersection:", set1)


intersection_set = set1.intersection(set2)
print("The intersection of set1 and set2 is:", intersection_set)

#intersection_set = set1 - set2