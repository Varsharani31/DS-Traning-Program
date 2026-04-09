# WAP Given an $M \times N$ matrix representing sales revenue for $N$ products over $M$ days, find the maximum revenue achieved each day.

m = int(input("Enter the number of days: "))
n = int(input("Enter the number of products: "))

matrix = []
for i in range(m):  
    row = list(map(int, input(f"Enter the revenue for products on day {i+1}: ").split()))
    matrix.append(row)

print("\nMaximum revenue achieved each day:")

for row in matrix:
    print(max(row), end=" ")
print()

# Output =
# Enter the number of days: 3
# Enter the number of products: 4
# Enter the revenue for products on day 1: 100 198 333 323
# Enter the revenue for products on day 2: 122 232 221 111
# Enter the revenue for products on day 3: 223 565 245 764
# Maximum revenue achieved each day:
# 333 232 764 