# WAP for change calculation with respect to Total Amount

amt = int(input("Enter the amount for withdrawal : "))
print("100 notes : ", amt // 100)
print("50 notes : ", (amt % 100) // 50)
print("20 notes : ", ((amt % 100) % 50) // 20)
print("10 notes : ", (((amt % 100) % 50) % 20) // 10)  
print("5 notes : ", ((((amt % 100) % 50) % 20) % 10) // 5)

# Output
# Enter the amount for withdrawal : 380 
# 100 notes :  3
# 50 notes :  1
# 20 notes :  1
# 10 notes :  1
# 5 notes :  0