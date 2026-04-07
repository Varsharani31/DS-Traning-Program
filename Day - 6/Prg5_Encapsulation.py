# if we declare variable as __a it is private variable
# If we declare variable as _a it is protected variable
# If we declare variable as a it is public variable
# Private variable is not accessible inside the child class

class Base:                                                 # Parent Class
    def __init__(self):
        print("Parent Class Constructor Called.")
        self.a = "Varsha"                                   # Public Variable
        self._b = "Pavankumar"                              # Protected Variable
        self.__c = "Kasliwal"                               # Private Variable

class Derived(Base):                                        # Child Class
    def __init__(self):
       Base.__init__(self)                                  # Parent Class Constructor Called.
       print("Calling Private Member of Base Class")
       print(self.a)                                        # Public Variable
       print(self._b)                                       # Protected Variable
       print(self.__c)                                      # Private Variable

obj1 = Derived()
print(obj1.a)
print(obj1._b)
print(obj1.__c)                                          

obj2 = Base()
print(obj2.a)
print(obj2._b)
print(obj2.__c)                                             
                                                            




# Output 1 =
# Parent Class Constructor Called.
# Calling Private Member of Base Class
# Varsha
# Traceback (most recent call last):
#   File "e:\DS Training Program\Day 6\Prg5_Encapsulation.py", line 18, in <module>
#     d = Derived()
#   File "e:\DS Training Program\Day 6\Prg5_Encapsulation.py", line 16, in __init__
#     print(self.__c)                                      # Private Variable
#           ^^^^^^^^
# AttributeError: 'Derived' object has no attribute '_Derived__c'



   # Output 2 = 
   # Parent Class Constructor Called.
   # Varsha
   # Traceback (most recent call last):
   #   File "e:\DS Training Program\Day 6\Prg5_Encapsulation.py", line 21, in <module>
   #     print(obj1.__c)
   #           ^^^^^^^^
   # AttributeError: 'Derived' object has no attribute '__c'


   # Output 3 =
   # Parent Class Constructor Called.
   # Varsha
   # Traceback (most recent call last):
   #   File "e:\DS Training Program\Day 6\Prg5_Encapsulation.py", line 31, in <module>
   #     print(obj2.__c)
   #           ^^^^^^^^
   # AttributeError: 'Base' object has no attribute '__c'