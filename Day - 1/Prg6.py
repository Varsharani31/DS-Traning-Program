# Swapping Using 3rd Variable

val1 = int(input("Enter Value 1st : "))
val2 = int(input("Enter Value 2nd : "))
print("Before Swapping Val1 = ",val1 , "val2 = ",val2)

temp = val1
val1 = val2
val2 = temp

print("After Swaping Val1 =",val1 , "Val2 = ",val2 )

# Output 

# Enter Value 1st : 100
# Enter Value 2nd : 200
# Before Swapping Val1 =  100 val2 =  200
# After Swaping Val1 = 200 Val2 =  100



# Swapping using 2 variables without using 3rd variable

val1 = int(input("Enter Value 1st : "))
val2 = int(input("Enter Value 2nd : "))
print("Before Swapping Val1 = ",val1 , "val2 = ",val2)

val1 = val1 + val2
val2 = val1 - val2
val1 = val1 - val2

print("After Swaping Val1 =",val1 , "Val2 = ",val2 )

# Output 

# Enter Value 1st : 100
# Enter Value 2nd : 200
# Before Swapping Val1 =  100 val2 =  200
# After Swaping Val1 = 200 Val2 =  100