# WAP using with statement to read and write in file

with open("WithFile.txt", "a") as f:
    f.write("\nVarsha")
    f.write("\nRani")
    f.write("\nManas")
    print("File is closed : ", f.closed)
print("File is closed : ", f.closed)


# Output = 
# File is closed :  False
# File is closed :  True

# WithFile.txt = 
# Varsha
# Rani
# Manas


with open("WithFile.txt", "r") as f:
  content = f.read()
  print(content)

# Output = 
# Varsha
# Rani
# Manas
# Varsha
# Rani
# Manas