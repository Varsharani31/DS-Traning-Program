# Abstraction means showing only essential features and hiding the unnecessary details
# A class which contain abstract method is called abstract class
# An abstract method that has declaration but no implementation is called abstract method
# Implementation is done in child class

from abc import ABC, abstractmethod

class help4Code(ABC):                                   # Abstract Class
    @abstractmethod                                     # Decorator
    def training(self):                                 # Abstract Method
        pass
    
    @abstractmethod                                     # Decorator
    def placement(self):                                # Abstract Method
        pass

class Ashish(help4Code):                                # Child Class
    def training(self):                                 # Abstract Method Implementation
        print("C , C++ ,  java")
    def placement(self):                                # Abstract Method Implementation
        print("Java Placement")

class Ankush(help4Code):                                # Child Class
    def training(self):                                 # Abstract Method Implementation
        print("Python | Django ")
    def placement(self):                                # Abstract Method Implementation
        print("Python Placement")

class Prashant(help4Code):                              # Child Class
    def training(self):                                 # Abstract Method Implementation
        print("Machine Learning ")
    def placement(self):                                # Abstract Method Implementation
        print("Data Science Placement")

a = Ashish()
a.training()
a.placement()

b = Ankush()
b.training()
b.placement()

p = Prashant()
p.training()
p.placement()



# Output =
# C , C++ ,  java
# Java Placement
# Python | Django 
# Python Placement
# Machine Learning 
# Data Science Placement