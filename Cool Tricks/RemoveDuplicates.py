### efficient way to remove duplicates from a list in Python using a set ###

## This method has a time complexity of O(n) because we only need to iterate over the list once, and a space complexity of O(n) because we are creating a new set and a new list. ##

l = [1, 2, 2, 3, 4, 2, 3, 5, 4, 3]

# convert the list to a set to remove duplicates
unique_set = set(l)

# convert the set back to a list
new_list = list(unique_set)

# print the new list without duplicates
print(new_list)