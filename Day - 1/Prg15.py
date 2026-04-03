# WAP to accept Physics Chemistry and Maths marks and calculate total and percentage and 
# if percentage is greater than 60 and gender is equal to male so he is eligible for placement else eligible for data entry job


physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))  
maths = int(input("Enter Maths marks: "))
gender = input("Enter your gender (male/female): ")

total = physics + chemistry + maths
percentage = total / 3.0 

print("Total marks:", total)
print("Percentage:", percentage)

if percentage > 60 and gender == "male":
    print("You are eligible for placement.")    
else:
    print("You are eligible for data entry job.")


# Output:
# Enter Physics marks: 70
# Enter Chemistry marks: 80 
# Enter Maths marks: 90
# Enter your gender (male/female):  male
# Total marks: 240  
# Percentage: 80.0
# You are eligible for placement.

# Enter Physics marks: 50
# Enter Chemistry marks: 30
# Enter Maths marks: 70
# Enter your gender (male/female): male
# Total marks: 150
# Percentage: 50.0
# You are eligible for data entry job.