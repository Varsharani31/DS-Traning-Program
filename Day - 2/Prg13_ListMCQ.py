# Q.1

arr = [[1,2,3,4],
       [4,5,6,7],
       [8,9,10,11],
       [12,13,14,15]]

# the pop() method removes the last item from the list and returns it. If the list is empty, it raises an IndexError.

for i in range(0,4):
    print(arr[i].pop())                 

# Output = 4
#          7    
#         11
#         15
              

# Q.2

arr = [1,2,3,4,5,6]

for i in range(1,6):
    arr[i - 1] = arr[i]     # arr[0] = arr[1] => arr[0] = 2
                            # arr[1] = arr[2] => arr[1] = 3
                            # arr[2] = arr[3] => arr[2] = 4
                            # arr[3] = arr[4] => arr[3] = 5
                            # arr[4] = arr[5] => arr[4] = 6
for i in range(0,6):
    print(arr[i], end=" ")                                       

# Output = 2
#          3
#          4
#          5
#          6
#          6


# Q.3

fruit_list1 = ["Apple","Berry","Cherry","Papaya"]
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = "Guava"
fruit_list3[1] = "Kiwi"

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
        if ls[0] == "Guava":                        # fruit_list1[0] = "Guava" => sum += 1
                                                    # fruit_list2[0] = "Guava" => sum += 1
                                                    # fruit_list3[0] = "Apple" => sum += 0
            sum += 1
        if ls[1] == "Kiwi":                         # fruit_list1[1] = "Berry" => sum += 0  
                                                    # fruit_list2[1] = "Berry" => sum += 0
                                                    # fruit_list3[1] = "Kiwi" => sum += 20              
            sum += 20
print(sum)     

# Output = 22


# Q.4

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[::2] = [10,20,30,40,50,60]                        
print(a)

# Output = ValueError: attempt to assign sequence of size 6 to extended slice of size 5

# Q.5

a = [1,2,3,4,5]
print(a[3:0:-1])                

# Output = [4, 3, 2]