# WAP to find common element in 2 list

my_list = [1,2,3,4,5]
my_list2 = [4,5,6,7,8]

for i in my_list:
    for j in my_list2:
        if i == j:
            print(i)

# Output = 4
#        = 5