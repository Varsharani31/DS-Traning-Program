# WAP to find security key for data

a = [5,7,8,3,7,8,9,2,3]
count = 0
freq_dict = {}

for item in a:
    freq_dict[item] = freq_dict.get(item, 0) + 1
    if freq_dict[item] > 1:
        count += 1
print("The security Key Is : ",count)                                            # Output = The security Key Is : 3