# WAP for Multi Level Inheritance

class College:                                  # Base Class (Parent Class) First - Level
    def college_name(self):                     # Method of Base Class
        print("Your College Name : YBIT")

class Student(College):                         # Second Class (Child Class) Second - Level
    def student_name(self):                     # Method of Second Class
        print("Your Student Name : Varsha")

class Exam(Student):                            # Third Class (Child Class) Third - Level
    def subject(self):                          # Method of Third Class
        print("Subject 1 : Python")
        print("Subject 2 : Java")
        print("Subject 3 : C++")

obj1 = Exam()                                   # Object of Derived Class
obj1.college_name()                             # Accessing Method of Base Class
obj1.student_name()                             # Accessing Method of Derived Class 1
obj1.subject()                                  # Accessing Method of Derived Class 2


# Output :
# Your College Name : YBIT
# Your Student Name : Varsha
# Subject 1 : Python
# Subject 2 : Java
# Subject 3 : C++