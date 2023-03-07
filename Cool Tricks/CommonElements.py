###  find the common elements between two lists ###

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

set1 = set(a)
set2 = set(b)

l = list(set1.intersection(set2))

print(l)