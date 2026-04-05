# WAP to Insert List In File


f = open("MyFile.txt", "w")
my_list = ["\nVarsha"," " ,"Rani"]
my_tuple = ("\nVarsha"," " ,"Rani")
my_dict = {"\nname":"Varsha","\nage":21}

f.writelines(my_list)
f.writelines(my_tuple)
f.writelines(my_dict)
# f.writelines(my_dict.values())
f.close()
print("File Operation is Done")

# Output = File Operation is Done

# myFile.txt = 
# Varsha Rani
# Varsha Rani
# name
# age
