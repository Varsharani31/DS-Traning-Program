class Student:
    roll_no = 101                                       # Data members

    def studentData(self):                              # Methods / Member Functions
        print("Student Information")

obj = Student()                                         # Creating an object

print(obj.roll_no)                                      # Accessing the data members

obj.studentData()                                       # Calling the methods



# Output = 101
#          Student Information


# Default Constructor is called internally if we not write constructor in a class.
# self variable is used to refer the current object. Self is default parameter of every method.