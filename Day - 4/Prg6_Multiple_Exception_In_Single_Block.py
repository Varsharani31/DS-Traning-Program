# WAP to handle multiple diffrent kinds of exception with Single Except Block

try:
    n1 = int(input("Enter first value : "))
    n2 = int(input("Enter second value : "))
    print(n1/n2)
except (ZeroDivisionError,ValueError) as msg:
    print(msg)


# Output =
# Enter first value : 4
# Enter second value : 2
# 2.0

# Enter first value : 3
# Enter second value : 0
# division by zero

# Enter first value : 2 
# Enter second value : @
# invalid literal for int() with base 10: '@'