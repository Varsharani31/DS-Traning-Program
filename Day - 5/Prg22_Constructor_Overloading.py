# WAP for constructor overloading

class Father:
    def __init__(self):
        print("Father := I am already at breakfast table")

class Child(Father):
    def __init__(self):
        print("Child := I will be late for the breakfast")
        super().__init__()

obj = Child()





# Output = Child := I will be late for the breakfast
#          Father := I am already at breakfast table




# Child class constructor override parent class constructor
# using super() we can access parent class constructor from child class constructor but there must be a parent-child relationship