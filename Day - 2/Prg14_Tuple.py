# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

mytuple = ("Varsha", "Rani", "Harsh",31,11)

print(mytuple)                                          # Output: ('Varsha', 'Rani', 'Harsh', 31, 11)
print(type(mytuple))                                    # Output: <class 'tuple'>                              

mytuple[0] = "Sneha"                                    # This will raise a TypeError because tuples are immutable (unchangeable)                         
print(mytuple)                                          # Output: TypeError: 'tuple' object does not support item assignment
