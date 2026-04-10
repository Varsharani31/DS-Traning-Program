# WAP to calculate the product of all the numbers in an array using recursion.

def product_of_array(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * product_of_array(arr[1:])

print(product_of_array([1, 2, 3, 10]))
print(product_of_array([1, 2, 3]))

# Output =
# 60
# 6
