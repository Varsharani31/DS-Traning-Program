# WAP to remove leading zeros from a list of numbers Input = [0, 0, 1, 2, 3, 0, 0, 4] Output = [1, 2, 3, 0, 0, 4]

def removeLeadingZeros(list):
    for i in range(len(list)):
        if list[i] != 0:
            return list[i:]
    return []

list = [0, 0, 1, 2, 3, 0, 0, 4]
print("Original list: ", list)
print("List after removing leading zeros: ", removeLeadingZeros(list))

# Output = 
# Original list:  [0, 0, 1, 2, 3, 0, 0, 4]
# List after removing leading zeros:  [1, 2, 3, 0, 0, 4]