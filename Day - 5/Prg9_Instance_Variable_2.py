# WAP for instance variable
# Declaring instance variable outside a class by using object

class Student:
    def __init__(self):                             # Constructor
        self.name = "Varsharani"
        self.roll_no = 101                          # Declaring a instance variable inside a constructor
       
    def get_data(self):                             # Method
        self.s_mb = 9876543210                      # Declaring a instance variable inside a method

obj1 = Student()
obj1.get_data()

del obj1.s_mb                                       # Deleting a instance variable using del keyword using object

obj1.s_branch = "CE"                                # Declaring a instance variable outside a class by using object

print(obj1.__dict__)                                # Printing a instance variable



# Output = {'name': 'Varsharani', 'roll_no': 101, 's_branch': 'CE'}

# __dict__ is a special attribute of a class that stores all the instance variables of a class.