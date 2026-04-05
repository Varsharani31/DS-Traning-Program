# WAP to read and write binary data in file

f1 = open("Panda.jpg", "rb")
f2 = open("Panda_Copy.jpg", "wb")

data = f1.read()
f2.write(data)

print("New image is available with the name : Panda_Copy.jpg")
f1.close()
f2.close()

# Output = New image is available with the name : Panda_Copy.jpg