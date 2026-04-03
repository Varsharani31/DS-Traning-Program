names = [4,2,5,6,8,2]

for i in names:
    print(i)  

# Output:
# 4
# 2
# 5
# 6
# 8
# 2


# Q.1 WAP to remove all the 0's from the list and add them at the end of the list.

# Method 1: Using list comprehension
a = [4,0,2,5,0,1]
b = []
c = []

for i in a:
    if i == 0:
        c.append(i)
    if i != 0:
        b.append(i)
print(b + c)                            # Output: [4, 2, 5, 1, 0, 0]


# Method 2: Using remove() and append() methods

a = [4,0,2,5,0,1]

for i in a:
    if i == 0:
        a.remove(i)
        a.append(i)
print(a)                                # Output: [4, 2, 5, 1, 0, 0]



# Q.2 WAP remove all the duplicates from the list and print the unique elements.

a = [1,2,2,3,4,4,5]
b = []

for i in a:
    if i not in b:
        b.append(i)
print(b)                                # Output: [1, 2, 3, 4, 5]



# Q.3 WAP to find out common elements from the three lists.

a = [1,2,3]
b = [2,3,4]
c = [3,4,5]

d = []

for i in a:
    if i in b and i in c:
        d.append(i)
print(d)                                # Output: [3]



# Q.4 WAP to calculate and return the sum of distances between the adjacent no. in an array of positive integers.

# Method 1  

a = int(input("Enter size of array : "))
b = []

for i in range(a):
    val = int(input("Enter the value of array : "))
    b.append(val)

sum = 0
print(b)                            

for i in range(a):
    if i + 1 in range(a):
        c = abs(b[i] - b[i+1])
    sum += c
print(sum)


# Output 

# Enter size of array : 5
# Enter the value of array : 11
# Enter the value of array : 31
# Enter the value of array : 7
# Enter the value of array : 3
# Enter the value of array : 2
# [11, 31, 7, 3, 2]
# 50


# Method 2 

a = int(input("Enter size of array : "))
b = []

for i in range(a):
     val = int(input("Enter the value of array : "))
     b.append(val)
for i in range(len(b)-1):
    b.append(abs(b[i+1] -  b[i]))
print(sum(b))                                   

# abs (absolute) convert negative value into positive value

# Output 

# Enter size of array : 5
# Enter the value of array : 11
# Enter the value of array : 31
# Enter the value of array : 2
# Enter the value of array : 7
# Enter the value of array : 3
# 112


# Q.5 WAP using break and continue statement

for i in range(1, 5):
    if i == 3:
        break
    print(i)                                
    
# # Output =
# 1
# 2

for i in range(1, 5):
    if i == 3:
        continue
    print(i)   


# Output =
# 1
# 2
# 4


# Q.6 WAP to print 1 2 4 5 and 5 4 2 1 using break and continue

# zip() function can take multiple range function

# Method 1 using zip()

for i,j in zip(range(1,6), range(5,0,-1)):
    if i == 3 and j == 3:
        continue
    print(i," ",j)

# Output:
# 1   5
# 2   4
# 4   2
# 5   1

# Method 2
for i in range(1, 6):
    if i == 3:
        continue
    print(i) 

print()

for i in range(5, 0, -1):
    if i == 3:
        continue
    print(i) 

# Output:
# 1
# 2
# 4
# 5

# 5
# 4
# 2
# 1



# Q.7 WAP to move *

a = "varsha*is*a*good*programmer"
b = ""
c = ""

for i in a:
    if i == "*":
       b += i 
    else:
       c += i
print(b+c)                          # Output = ****varshaisagoodprogrammer



# Q.8 Using BODMAS

a = 50
b = 30
c = 20
d = 10

print((a+b)*c/d)            # Output = 160.0
print((a-b)*c/d)            # Output = 40.0
print(a+(b*c)/d)            # Output = 110.0



# Q.9 

X = ['A','B','C']
Y = ['A','B','C']
Z = [1,2,3,4]

print(X == Y)           # Output = True
print(X == Z)           # Output = False
print(X != Z)           # Output = True



# Q.10 WAP to check if 2 strings are anagrams of each other

a = "listen"
b = "silent"

if sorted(a) == sorted(b):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Output = The strings are anagrams.



# Q.11 WAP to count words in a string

a = "This is a sentence"
count = 1
for i in a:
    if i == " ":
        count += 1

print("Number of words in the string:", count )                  # Output = Number of words in the string: 4




# Q.12 Given an array, return an array where each element is the product of all elements in the array except itself

a = [1,2,3,4]
b = []

for i in range(len(a)):
    product = 1
    for j in range(len(a)):
        if i != j:
            product *= a[j]
    b.append(product)
print(b)                                            # Output = [24, 12, 8, 6]