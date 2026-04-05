# WAP to Append In File (Adds to the file didn't overwrite)

f = open("file.txt", "a")
f.write("\nI am from Kharepatan.")
f.close()
print("File Operation is Done")


# Output = File Operation is Done

# file.txt = My name is Varsharani.
#            I am from Kharepatan.