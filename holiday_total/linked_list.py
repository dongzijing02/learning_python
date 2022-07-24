
class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<Node data: %s>' % self.data

# N1 = Node(10)
# print(N1)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        # 在开头加数值
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def ReverseLinkList(self):

        if self.head is None:
            return None

        while self.head is not None:
            if self.next is None:
                return self.head
            if self.next is not None:
                cur = self.head
                self.head = next
                next = next.next
                self.head.next = self.cur

        return self.head




l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
print(l)
