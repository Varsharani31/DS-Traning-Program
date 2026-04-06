# WAP for parameterize constructor

class Hod:
    def __init__(self,name,age,roll_no):                        # Parameterize Constructor
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def show(self):                                             # Instance Method
        print("My Name Is :", self.name)
        print("My Age Is :", self.age)
        print("My Roll No Is :", self.roll_no)

obj1 = Hod("Varsharani", 21, 1001)                              # Creating an object
obj1.show()                                                     # Calling the method


# Output =
# My Name Is : Varsharani
# My Age Is : 21
# My Roll No Is : 1001