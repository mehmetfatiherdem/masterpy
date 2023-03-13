### Strings in Python ###

## The keyword "in" can be utilized to verify whether a particular phrase or character exists within a given string.

txt = "Time is money"

# print("money" in txt) #prints True

#if "money" in txt:
    #print("Yes, 'money' is present")

#print("cheap" not in txt) # prints True

#if "cheap" not in txt:
    #print("No, 'cheap' is NOT present")

## String Slicing

## start including:stop including:step
## starts from 0 by default

a = "Hello, World!"
#print(a[3:8]) # lo, W

#print(a[:5]) # Hello

#print(a[7:]) # World!

#print(a[-5:-2]) # orl

#print(a[1:9:2]) # el,W


### Modify Strings ###

t = "Hello, World!"

#HELLO, WORLD!
print(t.upper())
#hello, world!
print(t.lower())

a = " hello, world! "

#hello, world!
print(a.strip())
#Jello, World!
print(t.replace("H", "J"))
#['Hello', ' World!']
print(t.split(","))

