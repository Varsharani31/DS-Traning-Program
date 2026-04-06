# WAP for instance variable

class New:
    def __init__(self):
        self.a = 10

obj1 = New()
obj2 = New()
obj3 = New()

print(obj1.a)
print(obj2.a)
print(obj3.a)

obj1.a = 20

print(obj1.a)
print(obj2.a)
print(obj3.a)


# Output =
# 10
# 10
# 10
# 20
# 10
# 10

# Instance variable is also called as object variable. It creates seprate memory for each object.
# If we want to change the value of one object then we can change it independently.
# Instance Variable is used in DS for linked list, graph, tree, stack, queue, etc.