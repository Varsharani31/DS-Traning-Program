# WAP to remove duplicates using for loop

name = "Varsha"
new_name = ""
for i in name:
    if i not in new_name:
        new_name += i
print(name)
print(new_name)

# Output:
# Varsha
# Varsh