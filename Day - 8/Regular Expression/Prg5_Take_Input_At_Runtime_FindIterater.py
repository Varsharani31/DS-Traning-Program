# WAP to find all the words in a string using finditer() method of regular expression by taking input from the user

import re

pattern = input("Enter the pattern: ")

matcher = re.finditer(pattern,input("Enter the string: "))

for i in matcher:
    print(i.start(),"......",i.end(),"......",i.group())


# Output = 
# Enter the pattern: e
# Enter the string: Hello
# 1 ...... 2 ...... e