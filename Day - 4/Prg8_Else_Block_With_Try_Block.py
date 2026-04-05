# WAP to handle multiple diffrent kinds of exception with Else Block

try:
    n1 = int(input("Enter first value : "))
    n2 = int(input("Enter second value : "))
    print(n1/n2)
except (ZeroDivisionError,ValueError) as msg:
    print("Enter Correct Number : ",msg)
else:
    print("This is else part of try block")


# Output =
# Enter first value : 2
# Enter second value : 3
# 0.6666666666666666
# This is else part of try block

# Enter first value : 2
# Enter second value : 0
# Enter Correct Number :  division by zero

# Enter first value : 2
# Enter second value : @
# Enter Correct Number :  invalid literal for int() with base 10: '@'