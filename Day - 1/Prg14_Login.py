# This program prompts the user to enter a username and password, and then check username and password are same then print "Login successful" otherwise print "Login failed"

username = input("Enter your username: ")
password = input("Enter your password: ")
if username == password:
    print("Login successful")
else:    
    print("Invalid Credential")


# Output:
# Enter your username: Varsha
# Enter your password: Varsha
# Login successful

# Enter your username: Varsha
# Enter your password: Varsh
# Invalid Credential
