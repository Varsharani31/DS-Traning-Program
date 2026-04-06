# WAP for Static Method

class Student:
    # By using class name we can access static method
    
    @staticmethod                                                   #decorator @staticmethod is used to define the static method
    def get_personal_details(firstname,lastname):
        print("Your personal details : ", firstname, lastname)

    @staticmethod
    def contact_details(mobile_no,roll_no):
        print("Your contact details : ", mobile_no, roll_no)


Student.get_personal_details("Varsha","Rani")
Student.contact_details(9876543210,1)


# Output :
# Your personal details :  Varsha Rani
# Your contact details :  9876543210 1