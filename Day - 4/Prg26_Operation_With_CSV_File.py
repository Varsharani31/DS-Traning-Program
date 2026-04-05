# WAP Operation with CSV File

import csv

f = open("student.csv","a",newline="")
a = csv.writer(f)
#a.writerow(["Student_ID","Roll_No","Name","Mobile_No"])
Stud_ID = int(input("Enter Student ID : "))
Roll_No = int(input("Enter Roll No : "))
Name = input("Enter Name : ")
Mobile_No = int(input("Enter Mobile No : "))
a.writerow([Stud_ID,Roll_No,Name,Mobile_No])
print("Record Added Successfully")
f.close()

# Output = 
# Enter Student ID : 1
# Enter Roll No : 1
# Enter Name : Varsha
# Enter Mobile No : 1234567890
# Record Added Successfully