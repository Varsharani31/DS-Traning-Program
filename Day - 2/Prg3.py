# Format Functions

print("Subject Marks : ")   # Output : Subject Marks :
phy = 50
chem = 60
math = 70

print("physics = {} chemistry = {} mathematics = {}".format(phy, chem, math))          # Output : physics = 50 chemistry = 60 mathematics = 70
print("physics = {0} chemistry = {1} mathematics = {2}".format(phy, chem, math))       # Output : physics = 50 chemistry = 60 mathematics = 70
print("physics = {x} chemistry = {y} mathematics = {z}".format(x=phy, y=chem, z=math)) # Output : physics = 50 chemistry = 60 mathematics = 70

total = phy + chem + math
print("Total Marks : ",f"{total}")      # Output : Total Marks :  180
print("Roll No = ", "14".zfill(4))      # Output : Roll No =  0014