# WAP for static variable

# Static variable is also called as class variable. It creates single memory for all objects.
# It does not depend on object.
# Static Variable is used in DS for linked list, graph, tree, stack, queue, etc.
# Two way to accesss Static Variable : 
                                        # 1. Using object
                                        # 2. Using class name

class New:  
    a = 10                          # Static Variable

    def __init__(self):
        self.b = "Varsha"           # Instance Variable

obj1 = New()
obj2 = New()
obj3 = New()

print(obj1.a)
print(obj2.a)
print(obj3.a)

New.a = 50

print(obj1.a)
print(obj2.a)
print(obj3.a)


# Output =
# 10
# 10
# 10
# 50
# 50
# 50
