### use enumerate() function to iterate over a sequence (such as a list) and keep track of the index of each item ###

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


print("************")

# You can also specify a start value for the index by passing a second argument to enumerate(). For example, if you want to start the index at 1 instead of 0, you can do this:

for index, fruit in enumerate(fruits, 1):
    print(f"{index}: {fruit}")