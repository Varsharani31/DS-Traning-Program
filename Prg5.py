# int() used to convert in integer

print(int(3.14)) # Output = 3
#print(int(10+5j))  # Output = Gives Error int() argument must be a string, a bytes-like object or a real number, not 'complex'
print(int(True))  # Output = 1
print(int(False))  # Output = 0
#print(int("4.22"))  # Output = Gives Error invalid literal for int() with base 10: '4.22'
print(int("4"))  # Output = 4


#float() used to convert 

print(float(3)) # Output = 3.0
# print(float(50+2j)) # Output = Gives Error float() argument must be a string or a real number, not 'complex'
print(float(True)) # Output = 1.0
print(float(False)) # Output = 0.0
print(float(4.22)) # Output = 4.22
print(float("4")) # Output = 4.0

# complex() used to convert

print(complex(3)) # Output = (3+0j)
print(complex(12.5)) # Output = (12.5+0j)
print(complex(True)) # Output = (1+0j)
print(complex(False)) # Output = 0j
print(complex("4.22")) # Output = (4.22+0j)
print(complex("4")) # Output = (4+0j)
#print(complex("name")) # Output = Gives Error ValueError: complex() arg is a malformed string 
print(complex(5,-3)) # Output = (5-3j)
print(complex(True,False)) # Output = (1+0j)


#bool() is used to convert

print(bool(0)) # Output = False
print(bool(15)) # Output = True
print(bool(3.14)) # Output = True
print(bool(0.0)) # Output = False
print(bool(1+2j)) # Output = True
print(bool(0+0j)) # Output = False
print(bool(-1)) # Output = True
print(bool(False)) # Output = False
print(bool(True)) # Output = True
print(bool("")) # Output = False
print(bool("Varsha")) # Output = True