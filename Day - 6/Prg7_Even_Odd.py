# WAP to get output like all odd no. comes after even no.

size = int(input("Enter the size of the list: "))
l = []

for _ in range(size):
    l.append(int(input("Enter a number: ")))

even = []
odd = []

for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("EVEN & ODD Numbers:", even + odd)


# Output = 
# Enter the size of the list: 8
# Enter a number: 10
# Enter a number: 98
# Enter a number: 3
# Enter a number: 33
# Enter a number: 12
# Enter a number: 22
# Enter a number: 21
# Enter a number: 11
# EVEN & ODD Numbers: [10, 98, 12, 22, 3, 33, 21, 11]