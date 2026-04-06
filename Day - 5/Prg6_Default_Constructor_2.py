# WAP for default constructor - Prg 2

class Hod:
    def __init__(self):                                         # Default Constructor
        self.name = "Varsharani"
        self.age = 21
        self.empid = 1001

    def info(self):                                             # Instance Method
        print("My Name Is :", self.name)
        print("My Age Is :", self.age)
        print("My EmpID Is :", self.empid)

obj1 = Hod()                                                    # Creating an object
obj1.info()                                                     # Calling the method


# Output =
# My Name Is : Varsharani
# My Age Is : 21
# My EmpID Is : 1001