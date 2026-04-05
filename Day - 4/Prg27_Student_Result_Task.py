# WAP to create a student result file and display the result of the student

import csv

f = open("student_result.csv","a",newline="")
a = csv.writer(f)
#a.writerow(["Roll_No","Name","Mobile_No","p1","p2","p3","Total","Percentage","Email","Result"])
Roll_No = int(input("Enter Roll No : "))
Name = input("Enter Name : ")
Mobile_No = int(input("Enter Mobile No : "))
p1 = int(input("Enter p1 : "))
p2 = int(input("Enter p2 : "))
p3 = int(input("Enter p3 : "))
Total = p1 + p2 + p3
Percentage = Total / 3
Email = input("Enter Email : ")

if Percentage >= 35:
    Result = "Pass" 
else:
    Result = "Fail"

a.writerow([Roll_No,Name,Mobile_No,p1,p2,p3,Total,Percentage,Email,Result])
print("Record Added Successfully")
f.close()
