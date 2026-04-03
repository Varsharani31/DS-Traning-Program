# Q1. What is the output of the following code snippet?

init_tuple = ()
print(init_tuple.__len__())                         # Output: 0             


# Q.2 What is the output of the following code snippet?

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')

print(type(init_tuple_a))                        # Output: <class 'tuple'>
print(type(init_tuple_b))                        # Output: <class 'tuple'>
print(id(init_tuple_a))                          # Output: 1779367536320
print(id(init_tuple_b))                          # Output: 1779367536320

print(init_tuple_a == init_tuple_b)              # Output: True


# Q.3 What is the output of the following code snippet?

init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')

print(init_tuple_a + init_tuple_b)                     # Output: ('1', '2', '3', '4')


# Q.4 What is the output of the following code snippet?

init_tuple_a = ('Python')*3
print(type(init_tuple_a))                              # Output: <class 'str'>


# Q.5 What is the output of the following code snippet?

# init_tuple_a = (1,)*3
# init_tuple_a[0] = 2
# print(init_tuple_a)                                  # Output : TypeError: 'tuple' object does not support item assignment


# Q.6 What is the output of the following code snippet?

init_tuple = ((1,2),) * 7                              # Output: ((1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2))
print(len(init_tuple[3:8]))                            # Output: 4  

