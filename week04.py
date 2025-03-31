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
        while current.next:
            current = current.link
        current.link = Node(data)


    def remove(self, target):
        current = self.head
        if self.head.data == target:
            self.head = self.head.link
            current.link = None
            return

        previous = None
        while current:
            if target == current.data:
                previous.link = current.link
                current.link = None
            previous = current
            current = current.link


    def search(self, target):
        current = self.head
        while current.next:
            if target == current.data:
                return f"{target}을(를) 찾았습니다!"
            else:
                current = current.next
        current.link = Node(target)


    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result = result + f"{current.data} -> "
            current = current.next
        return result + "END"


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)


print(ll)
print(ll.search(99))
print(ll.search(10))
ll.remove(8)
print(ll)

