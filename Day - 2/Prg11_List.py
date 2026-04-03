# List Functions in Python

my_list = ["Varsha","Rani",31,11,"Harsh","Pooja","Pavankumar"]

print(my_list)          # Output: ['Varsha', 'Rani', 31, 11, 'Harsh', 'Pooja', 'Pavankumar']
print(type(my_list))    # Output: <class 'list'>
print(my_list[0])       # Output: Varsha
print(my_list[1])       # Output: Rani
print(my_list[2])       # Output: 31
print(my_list[-1])      # Output: Pavankumar
print(my_list[2:5])     # Output: [31, 11, 'Harsh']
print(my_list[:5])      # Output: ['Varsha', 'Rani', 31, 11, 'Harsh']
print(my_list[1:])      # Output: ['Rani', 31, 11, 'Harsh', 'Pooja', 'Pavankumar']
print(my_list[1:8:2])   # Output: ['Rani', 11, 'Pooja']
print(my_list[:])       # Output: ['Varsha', 'Rani', 31, 11, 'Harsh', 'Pooja', 'Pavankumar']
print(my_list[::-1])    # Output: ['Pavankumar', 'Pooja', 'Harsh', 11, 31, 'Rani', 'Varsha']


# Change value 

my_list[2]  = 7
print(my_list)          # Output: ['Varsha', 'Rani', 07, 11, 'Harsh', 'Pooja', 'Pavankumar']


# Check the value is presnt in list or not

if "Varsha" in my_list:
    print("Yes Varsha is available")
else:
    print("Varsha is not available")     # Output = Yes Varsha is available


# Append Value in the list 

my_list.append(31)
print(my_list)        # Output = ['Varsha', 'Rani', 31, 11, 'Harsh', 'Pooja', 'Pavankumar', 31]


# Insert Value in the list

my_list.insert(1,"Riya")
print(my_list)              # Output = ['Varsha', 'Riya', 'Rani', 7, 11, 'Harsh', 'Pooja', 'Pavankumar', 31]


# Remove Value from the list 

my_list.remove("Riya")
print(my_list)              # Output = ['Varsha', 'Rani', 7, 11, 'Harsh', 'Pooja', 'Pavankumar', 31]


# Create Copy of existing List

newlist = my_list.copy()
print(newlist)              # Output = ['Varsha', 'Rani', 7, 11, 'Harsh', 'Pooja', 'Pavankumar', 31]



