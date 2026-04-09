# WAP to find the pattern in the string using match() method of regular expression

# match() method always search the pattern at the beginning of the string or at the first position

import re

pattern = input("Enter the pattern to perform match operation : ")

matcher = re.match(pattern,"Python is very important language.")
print(matcher)

if matcher != None:
    print("Pattern found")
    print(matcher.start(),"......",matcher.end())
else:
    print("Pattern not found")



# Output = 
# Enter the pattern to perform match operation : Python
# <re.Match object; span=(0, 6), match='Python'>
# Pattern found
# 0 ...... 6

# Enter the pattern to perform match operation : is
# None
# Pattern not found