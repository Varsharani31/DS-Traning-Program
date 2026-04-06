# WAP for method overriding

# Python Supports Method Overriding.
# Method Overriding is nothing but same method name in parent and child class.

class rbi:
    def home_loan(self):
        print("Home Loan = 7.5")
    def car_loan(self):
        print("Car Loan = 8 %")

class sbi(rbi):
    def home_loan(self):
        print("SBI Provide Home Loan = 6.5 %")      # Output = SBI Provide Home Loan = 6.5 %
        super().home_loan()                         # Output = Home Loan = 7.5 %

obj = sbi()
obj.home_loan()                                     # Child class method override parent class method



# using supper() we can access parent class method from child class method but there must be a parent-child relationship