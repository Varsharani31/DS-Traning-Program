# WAP to find all the words in a string using finditer() method of regular expression without using compile() method

import re

count = 0

matcher = re.finditer("function","A function in python is defined by a def statement. function is a block of code that performs a specific task. function is very important in python.")

for i in matcher:
    count += 1
    print(i.start(),"......",i.end(),"......",i.group())

print("The number of occurrences of the word 'function' is: ", count)



# Output = 
# 2 ...... 10 ...... function
# 52 ...... 60 ...... function
# 111 ...... 119 ...... function
# The number of occurrences of the word 'function' is:  3