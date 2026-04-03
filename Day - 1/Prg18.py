# Accept any character and digits uppercase or lowercase using ascii values 

char = ord(input("Enter a character: "))
if (char >= 48 and char <= 57):
    print("You entered a digit.")
elif (char >= 65 and char <= 90):
    print("You entered an uppercase letter.")
elif (char >= 97 and char <= 122):
    print("You entered a lowercase letter.")
else:
    print("You entered a special character.")


# Output:
# Enter a character: A
# You entered an uppercase letter.
# Enter a character: a
# You entered a lowercase letter.
# Enter a character: 5
# You entered a digit.
# Enter a character: @
# You entered a special character.