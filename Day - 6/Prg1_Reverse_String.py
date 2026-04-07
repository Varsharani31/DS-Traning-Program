# WAP to reverse each word in a string

a = "Hello World"
b = a.split()

for i in range(len(b)):
    b[i] = b[i][::-1]
    
print(" ".join(b))


# Output = olleH dlroW