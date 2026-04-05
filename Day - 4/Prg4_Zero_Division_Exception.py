# WAP Of Zero Division Exception Handling

n1 = int(input("Enter first value : "))
n2 = int(input("Enter second value : "))
try:
    print(n1/n2)
except:
    print("Not Divide By Zero.")
print("To be continue")


# Output =
# Enter first value : 2
# Enter second value : 0
# Not Divide By Zero.
# To be continue

# Enter first value : 4
# Enter second value : 2
# 2.0
# To be continue