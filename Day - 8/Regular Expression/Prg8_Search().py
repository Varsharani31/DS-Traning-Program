# WAP to find the pattern in the string using search() method of regular expression

# search() method if the match found anywhere in the string then it will return the match object else it will return None

import re

pattern = input("Enter the pattern to perform search operation : ")

matcher = re.search(pattern,"Python is very important language.")
print(matcher)

if matcher != None:
    print("Pattern found")
    print(matcher.start(),"......",matcher.end())
else:
    print("Pattern not found")


# Output = 
# Enter the pattern to perform search operation : Python
# <re.Match object; span=(0, 6), match='Python'>
# Pattern found
# 0 ...... 6

# Enter the pattern to perform search operation : is
# <re.Match object; span=(1, 3), match='is'>
# Pattern found
# 1 ...... 3

# Enter the pattern to perform search operation : language
# <re.Match object; span=(21, 29), match='language'>
# Pattern found
# 21 ...... 29