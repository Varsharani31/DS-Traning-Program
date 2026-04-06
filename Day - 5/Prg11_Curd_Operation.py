# WAP for CURD Operation

#first menu driven add student show student update student delete student exit then select choice 

# if choice is 1 then add student
    # add student_id
    # add Student_roll_no 
    # add Name
    # add city

# if choice is 2 then show student
    # show all student in table format

# if choice is 3 then update student
    # Enter student_id :
    # Matched Student Data are :
        # Student_roll_no 
        # Name
        # city
        # dont want to update

# if choice is 4 then delete student
    # Enter student_id :
    # Matched Student Data are :
        # Student_roll_no 
        # Name
        # city
        # dont want to delete

        # do you really want to delete this record (y/n) : 
        # if y then delete
        # if n then exit

# if choice is 5 then exit


import sys

class Student:
    def __init__(self):
        print("Student Management System")
        self.Stud_id = []
        self.Stud_roll_no = []
        self.Stud_name = []
        self.Stud_city = []

    def adddata(self):
        self.Stud_id.append(input("Enter Student ID : "))
        self.Stud_roll_no.append(input("Enter Student Roll No : "))
        self.Stud_name.append(input("Enter Student Name : "))
        self.Stud_city.append(input("Enter Student City : "))

    def showData(self):
        for i in range(len(self.Stud_id)):
            print(self.Stud_id[i], "\t\t", self.Stud_roll_no[i], "\t\t", self.Stud_name[i], "\t\t", self.Stud_city[i])            
        # \t is used to print the tab space

            for x in range(60):
                print("-", end="")
            print()

    def updateData(self):
        id = input("Enter Student ID : ")
        if id in self.Stud_id:
            index = self.Stud_id.index(id)              # it is used to find the index of the element
            print("Matched Found :")
            print("Student ID : ", self.Stud_id[index])
            print("Student Roll No : ", self.Stud_roll_no[index])
            print("Student Name : ", self.Stud_name[index])
            print("Student City : ", self.Stud_city[index])
            a = input("Do You Really Want To Update : (y/n) ")

            if a == 'y' or a == 'Y':
                self.Stud_id[index] = input("Enter Student ID : ")
                self.Stud_roll_no[index] = input("Enter Student Roll No : ")
                self.Stud_name[index] = input("Enter Student Name : ")
                self.Stud_city[index] = input("Enter Student City : ")
            else:
                pass
        else:
            print("No Matched Found")

    
    def deleteData(self):
        id = input("Enter Student ID : ")
        if id in self.Stud_id:
            index = self.Stud_id.index(id)
            print("Matched Found :")
            print("Student ID : ", self.Stud_id[index])
            print("Student Roll No : ", self.Stud_roll_no[index])
            print("Student Name : ", self.Stud_name[index])
            print("Student City : ", self.Stud_city[index])
            a = input("Do You Really Want To Delete : (y/n) ")
            if a == 'y' or a == 'Y':
                self.Stud_id.pop(index)
                self.Stud_roll_no.pop(index)
                self.Stud_name.pop(index)
                self.Stud_city.pop(index)
            else:
                pass
        else:
            print("No Matched Found")


    def exit(self):
        sys.exit()



    def MenuDriven(self):
        while True:
            print("\n1. Add Student")
            print("2. Show Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = int(input("Enter Your Choice : "))
            if choice == 1:
                self.adddata()
            elif choice == 2:
                self.showData()
            elif choice == 3:
                self.updateData()
            elif choice == 4:
                self.deleteData()
            elif choice == 5:
                self.exit()
            else:
                print("Invalid Choice")

obj1 = Student()
obj1.MenuDriven()