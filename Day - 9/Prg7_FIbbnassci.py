# WAP to calculate the nth Fibonacci number using recursion.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))

# Output =
# 3