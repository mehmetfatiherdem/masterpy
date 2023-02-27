### Use List Comprehension to Create a new List ###

## Create a list of numbers
numbers = [1,2,3,4,5]

## Use a list comprehension to create a new list of squares
squares = [x**2 for x in numbers]

## Print the new list of squares
print(squares)

## Use a list comprehension to create a new list of even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

## Print the new list of even numbers
print(even_numbers)