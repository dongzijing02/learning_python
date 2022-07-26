class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverseLinkList(self):
        current = self.head
        temp = None
        if self.head is None:
            return None
        while current is not None:
            next_node = current.next
            current.next = temp
            temp = current
            current = next_node
        self.head = temp

        return llist.printList()

    def partlyReverseLinkedlist(self):
        current = self.head
        dummyHead = Node(0)
        dummyHead.next = current
        pre = dummyHead
        if self.head is None:
            return None
        while current is not None:
            next_node = current.next
            next2_node = next_node.next
            if next2_node is not None:
                pre.next = next_node
                current.next = next2_node
                next_node.next = current
                pre = current
                current = next2_node
                next_node = current.next
                next2_node = next_node.next
            if next2_node is None: 
                pre.next = next_node
                current.next = next2_node
                next_node.next = current
                pre = current
                current = next2_node

        return dummyHead.next

    def printList(self):  # 打印链表
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


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
llist.head.next = second  # 建立指针使前一个指向后一个
second.next = third
third.next = fourth
# print(llist.reverseLinkList())
print(llist.printList())
llist.partlyReverseLinkedlist()
print(llist.printList())
