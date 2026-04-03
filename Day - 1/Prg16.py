# WAP to accept value of A , B , C and check find max value using nested if else statement

A = float(input("Enter the value of A: "))
B = float(input("Enter the value of B: ")) 
C = float(input("Enter the value of C: "))

if A > B:
    if A > C:
        print("The maximum value is A:", A)
    else:
        print("The maximum value is C:", C)
else:
    if B > C:
        print("The maximum value is B:", B)
    else:
        print("The maximum value is C:", C)


# Output:
# Enter the value of A: 11
# Enter the value of B: 31
# Enter the value of C: 15
# The maximum value is B: 31.0