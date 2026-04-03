# Multidimensional List Functions in Python

mylist = [["Varsha",31],["Rani",7],["Harsh",4]]

print("example of multidimentional list : ")        # Output = example of multidimentional list : 
print(mylist)                                       # Output = [['Varsha', 31], ['Rani', 7], ['Harsh', 4]]
# print(mylist[row][col])
print(mylist[0][0])                                 # Output = Varsha
print(mylist[0][1])                                 # Output = 31
print(mylist[1][0])                                 # Output = Rani
print(mylist[1][1])                                 # Output = 7
print(mylist[2][0])                                 # Output = Harsh
print(mylist[2][1])                                 # Output = 4


# List Repetition

list1 = ["Varsha","Rani"]
print(list1*2)                                      # Output = ['Varsha', 'Rani', 'Varsha', 'Rani']

# List Concatenation

list2 = [50,60.40]
print(list1 + list2)                                # Output = ['Varsha', 'Rani', 50, 60.4]


# Delete the list

del list2[1]
print(list2)                                        # Output = [50]

del list2
print(list2)                                        # Output = NameError: name 'list2' is not defined. Did you mean: 'list1'?


# Clear the list

list2.clear()
print(list2)                                        # Output = []

# List typecasting

name = "Varsha"                                     
print(name)                                         # Output = Varsha
myname = list(name)
print(myname)                                       # Output = ['V', 'a', 'r', 's', 'h', 'a']

# List Reverse 

mylist = [1,2,3,4,5]
mylist.reverse()
print(mylist)                                       # Output = [5, 4, 3, 2, 1]

# List Sort
list3 = [5,2,3,1,4]
list3.sort()
print(list3)                                       # Output = [1, 2, 3, 4, 5]

# List Aliasing

mylist = [1,2,3,4,5]
newlist = mylist
print(newlist)                                         # Output = [1, 2, 3, 4, 5]
print(id(newlist))                                     # Output = 1921378006720
print(id(mylist))                                      # Output = 1921378006720
mylist[0] = 10
print(mylist)                                          # Output = [10, 2, 3, 4, 5]
print(newlist)                                         # Output = [10, 2, 3, 4, 5]