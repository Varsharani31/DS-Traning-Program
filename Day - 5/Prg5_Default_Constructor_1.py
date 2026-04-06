# WAP to create default constructor in a class

class Demo:
    def __init__(self):
        print("I am Constructor :")

    def msg(self):
        print("Hello Class !")

obj1 = Demo()                                   # Creating an object. For one object constructor is called once
print(obj1)                                     # Output = <__main__.Demo object at 0x0000028B06E78C20>

obj2 = Demo()                                   # Creating another object. For second object constructor is called once

obj1.msg()                                      # Calling the method

# del obj1                                        # Deleting an object



# Output =
# I am Constructor :
# <__main__.Demo object at 0x000002246B898C20>
# I am Constructor :
# Hello Class !