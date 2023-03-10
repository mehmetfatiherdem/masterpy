### Strings in Python ###

## The keyword "in" can be utilized to verify whether a particular phrase or character exists within a given string.

txt = "Time is money"

print("money" in txt) #prints True

if "money" in txt:
    print("Yes, 'money' is present")

print("cheap" not in txt) # prints True

if "cheap" not in txt:
    print("No, 'cheap' is NOT present")
    