# WAP for Instance Method

class Student:
    def __init__(self, name, roll_no,mobile_no):
        self.name = name                                # Instance Variable
        self.roll_no = roll_no
        self.mobile_no = mobile_no

    def display(self):                                   # Instance Method
        print(self.name,self.roll_no,self.mobile_no)                    

obj1 = Student("Varsha", 1, 9876543210)
obj1.display()


# Instance Method means writing Instance Variable in Method


# Output : Varsha 1 9876543210