from abc import ABC, abstractmethod

class Irctc(ABC):                                           # Abstract Class
    @abstractmethod                                         # Decorator
    def BookTicket(self):                                   # Abstract Method
        pass

class MakeMyTrip(Irctc):                                    # Child Class
    def BookTicket(self):                                   # Abstract Method Implementation
        print("=======================================")
        print("  Welcome to MakeMyTrip ")
        source = input("Enter Source : ")
        destination = input("Enter Destination : ")
        date = input("Enter Date : ")
        print("=======================================")

class Goibibo(Irctc):                                       # Child Class
     def BookTicket(self):                                  # Abstract Method Implementation
        print("=======================================")
        print("  Welcome to Goibibo ")
        source = input("Enter Source : ")
        destination = input("Enter Destination : ")
        date = input("Enter Date : ")

class Yatra(Irctc):                                         # Child Class
      def BookTicket(self):                                 # Abstract Method Implementation
        print("=======================================")
        print("  Welcome to Yatra ")
        source = input("Enter Source : ")
        destination = input("Enter Destination : ")
        date = input("Enter Date : ")

m = MakeMyTrip()
m.BookTicket()

g = Goibibo()
g.BookTicket()

y = Yatra()
y.BookTicket()



# Output = 
# =======================================
#   Welcome to MakeMyTrip 
# Enter Source : Mumbai
# Enter Destination : Dapoli
# Enter Date : 23 - 04 - 26
# =======================================
# =======================================
#   Welcome to Goibibo 
# Enter Source : Mumbai      
# Enter Destination : Dapoli
# Enter Date : 23 - 04 - 26
# =======================================
#   Welcome to Yatra
# Enter Source : Mumbai      
# Enter Destination : Dapoli
# Enter Date : 23 - 04 - 26