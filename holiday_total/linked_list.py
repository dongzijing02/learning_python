class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def ReverseLinkList(self):
        if self.head is None:
            return None
        while self.head is not None:
            if self.next is None:
                return self.head
            if self.head.next is not None:
                cur = self.head
                self.head = self.head.next
                self.head.next = self.head.next.next
                self.head.next = cur
        return self.head

    def printList(self):  # 建立链表
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    #
    # def push(self, new_data):  # 新节点总是添加在给定链表的头部之前。新添加的节点成为链表的新头
    #     new_node = Node(new_data)
    #     new_node.next = self.head
    #     self.head = new_node
    #
    # # 在指定节点后插入
    # def insert(self, prev_node, new_data):
    #     if prev_node is None:
    #         return
    #     new_node = Node(new_data)
    #     new_node.next = prev_node.next
    #     prev_node.next = new_node
    #
    # # 在结尾加
    # def append(self, new_data):
    #     new_node = Node(new_data)
    #     if self.head is None:
    #         self.head = new_node
    #         return
    #     last = self.head
    #     while last.next:
    #         last = last.next
    #     last.next = new_node
    #
    # def deleteNode(self, key):
    #     temp = self.head
    #     if temp is not None:
    #         if temp.data == key:
    #             self.head = temp.next
    #             temp = None
    #             return
    #     while temp is not None:
    #         if temp.data == key:
    #             break
    #         prev = temp
    #         temp = temp.next
    #     if temp is None:
    #         return
    #     prev.next = temp.next
    #     temp = None


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second  # 建立指针使前一个指向后一个
    second.next = third:

print(llist.printList())
print(llist.ReverseLinkList())
