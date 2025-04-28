
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        self._size += 1
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node



q = Queue()
q.enqueue("Data structure")
q.enqueue("Database")
<<<<<<< HEAD
print(q._size, q.front.data, q.rear.data)
=======
print(q._size, q.front.data, q.rear.data)


>>>>>>> 1cabd55ee7a1774fe12053f15936e4e466ffdda5
