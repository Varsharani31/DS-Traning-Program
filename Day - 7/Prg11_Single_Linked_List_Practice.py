# WAP to create a single linked list

class Node:
    def __init__(self,data):
        self.data = data                                    # Instance Variable
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

linkedList = LinkedList()
linkedList.head = Node(5)                                   # First Node is Created
second          = Node(10)                                  # Second Node is Created
third           = Node(15)                                  # Third Node is Created
fourth          = Node(20)                                  # Fourth Node is Created


# Linking Part

linkedList.head.next = second
second.next = third
third.next = fourth

print(linkedList.head.data)
print(second.data)
print(third.data)
print(fourth.data)


print(linkedList.head.next)
print(second.next)
print(third.next)
print(fourth.next)


# Display LinkedList

while linkedList.head != None:
    print("|",linkedList.head.data,"|",linkedList.head.next, end = " ----> ")
    linkedList.head = linkedList.head.next

    