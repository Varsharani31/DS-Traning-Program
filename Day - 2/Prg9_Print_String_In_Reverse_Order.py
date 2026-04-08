# WAP to print string in reverse order using for loop

# Method 1: Using slicing

name = "Mumbai"
new_name = ""
for i in name[::-1]:
    new_name += i
print(new_name)

# Output:
# iabmuM

# Method 2: Using range and indexing

name = "Mumbai"
new_name = ""
for i in range(len(name)-1,-1,-1):
   new_name += name[i]
print(new_name)

# Output:
# iabmuM
