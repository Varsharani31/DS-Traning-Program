# WAP to compress the string by replacing consecutive characters with the character and its count

l = ["a", "a", "a", "b", "b", "c", "c", "c", "c"]

comp = ""
count = 1

for i in range(1, len(l)):
    if l[i] == l[i-1]:
        count += 1
    else:
        comp += l[i-1] + str(count)
        count = 1

comp += l[-1] + str(count)

print("Output =", comp)


# Output = a3b2c4