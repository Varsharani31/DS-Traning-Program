# WAP palindrome or not using for loop

name = "racecar"
new_name = ""
for i in name[::-1]:
    new_name += i

print("Name : ",name)
if name == new_name:
    print(name," is a Palindrome")
else:
    print(name," is not a Palindrome")

# Output:
# Name :  racecar
# racecar is a Palindrome


# WAP palindrome or not using if

name = "python"
new_name = name[::-1]   
print("Name : ",name)
if name == new_name:
    print(name," is a Palindrome")
else:
    print(name," is not a Palindrome")

# Output:
# Name :  python    
# python is not a Palindrome