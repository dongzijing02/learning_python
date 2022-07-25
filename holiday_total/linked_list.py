
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
    def __init__(self, value):
        self.head = None
        self.value = value

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # def ReverseLinkList(self):
    #
    #     if self.head is None:
    #         return None
    #     while self.head is not None:
    #         if self.next is None:
    #             return self.head
    #         if self.head.next is not None:
    #             cur = self.head
    #             self.head = self.head.next
    #             self.head.next = self.head.next.next
    #             self.head.next = cur
    #             print(cur)
    #
    #     return self.head.data

    def print_link_list(self):
        li = []
        self.head.next = next
        if self.head is None:
            return None
        while self.head is not None:
            li.append(self.head)
            if self.head.next is None:
                return li
            if self.head.next is not None:
                li.append(self.head.next)
                self.head = self.head.next
                return li


l = LinkedList(0)
l.add(1)
l.add(2)
l.add(3)
l.add(4)
print(l)
print(l.print_link_list())
