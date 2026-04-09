# WAP to find all the words in a string using finditer() method of regular expression

import re

count = 0

patter = re.compile("function")

matcher = patter.finditer("A function in python is defined by a def statement. function is a block of code that performs a specific task. function is very important in python.")

for i in matcher:
    count += 1
    print(i.start(),"......",i.end(),"......",i.group())

print("The number of occurrences of the word 'function' is: ", count)


# Output = 
# 2 ...... 10 ...... function
# 52 ...... 60 ...... function
# 111 ...... 119 ...... function
# The number of occurrences of the word 'function' is:  3