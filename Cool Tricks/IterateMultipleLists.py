### Iterate Multiple Lists With zip() ###

names = ['Emma', 'John', 'Jane']
ages = [30, 22, 25]

for name, age in zip(names, ages):
    print(f'{name} is {age} years old')

# Calculate the dot product using zip()

x = [1, 2, 3]
y = [4, 5, 6]

dot_product = sum(xi * yi for xi, yi in zip(x, y))

print(dot_product)