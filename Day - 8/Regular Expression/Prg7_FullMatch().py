# WAP to find the pattern in the string using fullmatch() method of regular expression

# fullmatch() use to match the pattern with the entire string

import re

pattern = input("Enter the pattern to perform fullmatch operation : ")

matcher = re.fullmatch(pattern,"Python is very important language.")
print(matcher)

if matcher != None:
    print("Pattern found")
    print(matcher.start(),"......",matcher.end())
else:
    print("Pattern not found")


# Output = 
# Enter the pattern to perform fullmatch operation : Python is very important language.
# <re.Match object; span=(0, 34), match='Python is very important language.'>
# Pattern found
# 0 ...... 34

# Enter the pattern to perform fullmatch operation : Python
# None
# Pattern not found