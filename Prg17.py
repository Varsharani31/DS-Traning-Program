# Accept Days if we enter monday - friday it will show working day and if we enter saturday and sunday it will show holiday

day = input("Enter the day: ")
if day == "Saturday" or day == "Sunday":
    print("Holiday")
else:
    print("Working day")

# Output:
# Enter the day: Monday 
# Working day

# Enter the day: Saturday
# Holiday
