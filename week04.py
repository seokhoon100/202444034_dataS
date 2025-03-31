import random
from traceback import print_tb


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)

    def search(self, target):
        current = self.head
        while current.link:
            if target == current.data:
                return f"{target}을(를) 찾았습니다!"
            else:
                current = current.link
        current.link = Node(target)

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result = result + f"{current.data} -> "
            current = current.link
        return result + "END"
        # return "Linked list!"

ll = LinkedList()
for _ in range(0, 20):
    ll.append(random.randint(1, 20))
print(ll)
print(ll.search(10))



# ll = LinkedList()
# ll.append(8)
# ll.append(10)
# ll.append(-9)

# print(ll)
# print(ll.search(99))
# print(ll.search(10))
