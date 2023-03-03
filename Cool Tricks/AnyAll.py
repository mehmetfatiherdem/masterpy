### use the any() and all() functions to test the truthiness of iterables ###

# Define some lists with truthy and falsy elements
l1 = [0, False, None, '', [], {}]
l2 = [1, True, 'ok', [1, 2], {'a': 1}]

# Test the truthiness of the lists using any() and all()
print(any(l1))   # False
print(any(l2))   # True
print(all(l1))   # False
print(all(l2))   # True