my_list = [1, 2, 2, 3, 1, 4, 2, 1, 5]
freq_dict = {}

for item in my_list:
    freq_dict[item] = freq_dict.get(item, 0) + 1

print(f"List: {my_list}")                       # Output = List: [1, 2, 2, 3, 1, 4, 2, 1, 5]
print(f"Frequency: {freq_dict}")                # Output = Frequency: {1: 3, 2: 3, 3: 1, 4: 1, 5: 1}