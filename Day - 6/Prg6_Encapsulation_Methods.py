class Rbi:
    def publicPolicy(self):                                         # Public Method
        print("Check the Public Policy of RBI.")
   
    def __privatePolicy(self):                                      # Private Method
        print("There is some private policy which is not accessible outside the class.")

class Sbi(Rbi):
    def __init__(self):                                             # Child Class Constructor
        Rbi.__init__(self)                                          # Parent Class Constructor Called.

    def callingPublicMethod(self):                                  # Public Method
        print("\nInside Child Class")
        self.publicPolicy()                                         # Public Method Called.
    
    def callingPrivateMethod(self):                                 # Public Method
        # print("\nInside Child Class")
        self.__privatePolicy()                                      # Private Method Called.

# obj = Sbi()
# obj.callingPublicMethod()
# obj.callingPrivateMethod()
# obj.publicPolicy()
# obj.__privatePolicy()

# obj1 = Rbi()
# obj1.publicPolicy()
# obj1.__privatePolicy()

# obj1 = Rbi()
# obj1.publicPolicy()
# obj1._Rbi__privatePolicy()


# Output =
# Inside Child Class
# Check the Public Policy of RBI.
# 
# Inside Child Class
# Traceback (most recent call last):
#   File "e:\DS Training Program\Prg6_Encapsulation_Methods.py", line 23, in <module>
#     obj.callingPrivateMethod()
#   File "e:\DS Training Program\Prg6_Encapsulation_Methods.py", line 20, in callingPrivateMethod
#     self.__privatePolicy()                                      # Private Method Called.
#     ^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'Sbi' object has no attribute '_Sbi__privatePolicy'   


# Output 2 = 
# Check the Public Policy of RBI.
# There is some private policy which is not accessible outside the class.