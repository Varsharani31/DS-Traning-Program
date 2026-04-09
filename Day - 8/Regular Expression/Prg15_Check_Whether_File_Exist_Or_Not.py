# WAP to check whether the file exist or not if exist print the content of the file else print file name not found.

import os,sys
file = input("Enter the File Name : ")
if os.path.exists(file):
    print("File Exists")
    f = open(file, "r")

else:
    print("File Not Found")
    sys.exit()

print("The Content of file is : ")
data = f.read()
print(data)



# Output =
# Enter the File Name : File.txt
# File Exists
# The Content of file is : 
# Function is a block of code which is used to perform a specific task.
# Function is very important in python.
# Function is a reusable code.


# Enter the File Name : File
# File Not Found