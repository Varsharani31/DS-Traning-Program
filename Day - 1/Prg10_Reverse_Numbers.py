# Reverse the No. 123

num = 123
a = num % 10 # 3
num = num // 10 # 12
b = num % 10 # 2
c = num // 10 # 1
rev = a*100 + b*10 + c 
print(rev) # Output = 321

# Reverse the No. 123456


num = 123456
a = num % 10 # Output = 6
num = num // 10 # Output = 12345
b = num % 10 # Output = 5
num = num // 10 # Output = 1234
c = num % 10 # Output = 4
num = num // 10 # Output = 123
d = num % 10 # Output = 3
num = num // 10 # Output = 12
e = num % 10 # Output = 2
num = num // 10 # Output = 1
rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + num # Output = 654321
print(rev)
