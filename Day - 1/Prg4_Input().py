
print(2+2)
print("2"+"2")
val1 = input("Enter value of val1 : ") #2
val2 = input("Enter value of val2 : ") #4
print(val1 + val2)

# Output 

# 4
# 22
# Enter value of val1 : 2
# Enter value of val2 : 4
# 24


#input() by default only accept only string value that's why we get output 24 after entering valu 2 & 4
#for this logical error write the input() inside int()

print(2+2)
print("2"+"2")
val1 = int(input("Enter value of val1 : ")) #2
val2 = int(input("Enter value of val2 : ")) #4

print(val1 + val2)

# Output
# 4
# 22
# Enter value of val1 : 2
# Enter value of val2 : 4
# 6
