# WAP to handle multiple diffrent kinds of exception with Default Except Block

try:
    n1 = int(input("Enter first value : "))
    n2 = int(input("Enter second value : "))
    print(n1/n2)
except (ZeroDivisionError,ValueError) as msg:
    print("Enter Correct Number : ",msg)
except:
    print("This is default part of except block")



# Output =
# Enter first value : 2
# Enter second value : 3
# 0.6666666666666666

# Enter first value : 2
# Enter second value : 0
# Enter Correct Number :  division by zero

# Enter first value : 2
# Enter second value : @
# Enter Correct Number :  invalid literal for int() with base 10: '@'