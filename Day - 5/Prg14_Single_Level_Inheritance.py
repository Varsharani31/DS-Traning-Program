# WAP for Single Inheritance

class College:                                  # Base Class (Parent Class)
    def college_name(self):                     # Method of Base Class
        print("Your College Name : YBIT")

class Student(College):                         # Derived Class (Child Class)
    def student_name(self):                     # Method of Derived Class
        print("Your Student Name : Varsha")

obj1 = Student()                                # Object of Derived Class
obj1.college_name()                             # Accessing Method of Base Class
obj1.student_name()                             # Accessing Method of Derived Class


# Output :
# Your College Name : YBIT
# Your Student Name : Varsha