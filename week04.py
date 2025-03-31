

def append(self, data):
    if not self.head:
        self.head = Node(data)
        return
    current = self.head
    while current.link:
        current = current.link
    current.link = Node(data)



li = linkedList()
li.append(8)
li.append(10)
li.append(-9)