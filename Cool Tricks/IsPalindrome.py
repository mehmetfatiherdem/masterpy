### check whether a given string is a palindrome or not ###

s = "A man, a plan, a canal: Panama"

s = "".join(c for c in s.lower() if c.isalnum())

is_palindrome = s == s[::-1]

print(is_palindrome)
