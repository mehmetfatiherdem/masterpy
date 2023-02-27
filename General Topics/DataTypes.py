### Data Types in Python ###

## integer
x = 5

## float
x = 5.5

## complex: means a number with a real and an imaginary part
x = 5 + 5j

## list
x = [1, 2, 3]
x = [1, "ok", 3.4]

## tuple: same as list but immutable(cannot be changed)
x = (1, "Hello", 3.4)

## range: range of number(starts from 0 by default)
x = range(5)

## dictionary: key-value pairs
x = {"name": "John", "age": 25}

## set: unordered collection of unique items
x = {"apple", "banana", "cherry"}
x = {1, "Hello", 2.3}
x = {1, "Hello", 1, 2} # will only print 1, Hello and 2(not going to print 1 twice)

## frozen set: same as set but immutable
x = frozenset({"Hello", "world", "!"})

## boolean: True or False
x = True

## string

# with double quotes
x = "This is string"
# with single quotes
x = 'This is string with single quotes'

# escape the single quote with \
x = 'This is a \'string\''
# escape the single quote with double quotes
x = "This is a 'string'"

# new line with \n
x = "Hello\nthis goes to the next line"

# multiline string with triple quotes
x = """This is a multiline string with triple quotes.
This is the second line.
This is the third line."""

#You can also use \ to break the line
x = """\
This is a multiline string with triple quotes.
This is the second line.
This is the third line.\
"""

## bytes: immutable sequence of integers in the range 0 <= x < 256
x = b"John"

## bytearray: mutable sequence of integers in the range 0 <= x < 256
x = bytearray(8)

## memoryview: memory view of a byte-like object
x = memoryview(bytes(8))

## None
x = None