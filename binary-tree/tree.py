# Tree
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#     def print_tree(self):
#         spaces = ' ' * self.get_level()
#         print(spaces + self.data)
#         if len(self.children) > 0:
#             for child in self.children:
#                 child.print_tree()
# def build_product_tree():
#     root = TreeNode("Electronics")
#     laptop = TreeNode("laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("surface"))
#     cellphone = TreeNode("cellphone")
#     cellphone.add_child(TreeNode("pixel"))
#     cellphone.add_child(TreeNode("oppo"))
#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("samsung"))
#     tv.add_child(TreeNode("lg"))
#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)
#     return root
# if __name__ == '__main__':
#     root = build_product_tree()
#     # print(root.get_level())
#     root.print_tree()
#     pass

class BinaryTree(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preorder_print(self):
        li = []
        if self is None:
            return None
        if self is not None:
            li.append(self.value)
        if self.left is not None:
            self.left.preorder_print()
            li = li + self.left.preorder_print()
        if self.right is not None:
            self.right.preorder_print()
            li = li + self.right.preorder_print()
        return li

    def get_node_count(self):
        l = 0
        r = 0
        if self is None:
            return 0
        if self.left is not None:
            l = self.left.get_node_count()
        if self.right is not None:
            r = self.right.get_node_count()
        return l + r + 1

    def find(self, value_to_find):
        l = False
        r = False
        if self is None:
            return False
        elif self.value == value_to_find:
            return True
        if self.left is not None:
            l = self.left.find(value_to_find)
        if self.right is not None:
            r = self.right.find(value_to_find)
        return l or r

    def get_height(self):
        L = 0
        R = 0
        if self is None:
            return 0
        if self.left is not None:
            L = self.left.get_height()
        if self.right is not None:
            R = self.right.get_height()
        return max(L, R) + 1

    def count_leaves(self):
        l = 0
        r = 0
        if self is None:
            return 0
        if self.right is None and self.left is None:
            return 1
        if self.left is not None:
            l = self.left.count_leaves()
        if self.right is not None:
            r = self.right.count_leaves()
        return l + r


tree = BinaryTree(1)
tree.left = BinaryTree(4)
tree.right = BinaryTree(5)
tree.left.left = BinaryTree(7)
tree.left.right = BinaryTree(8)
tree.right.left = BinaryTree(9)
tree.right.right = BinaryTree(10)
tree.left.left.left = BinaryTree(6)
tree.left.right.right = BinaryTree(12)
#
# tree2 = BinaryTree(1)
# tree2.root.left = Node(4)
# tree2.root.right = Node(5)
# tree2.root.left.left = Node(7)
# tree2.root.left.right = Node(8)
# tree2.root.right.left = Node(9)
# tree2.root.right.right = Node(10)
# tree2.root.left.left.left = Node(6)
# tree2.root.left.right.right = Node(12)
# tree2.root.left.left.right = Node(4)
# # tree2.root.left.left.left.left = Node(3)

# tree3 = BinaryTree(1)
# tree3.root.left = Node(2)
# tree3.root.right = Node(2)
# tree3.root.left.right = Node(5)
# tree3.root.left.left = Node(4)
# tree3.root.right.right = Node(4)
# tree3.root.right.left = Node(5)

# print(tree.is_same(tree.root, tree2.root))
T = tree.preorder_print()
print(T)
print(tree.find(40))
print(tree.get_height())
print(tree.get_node_count())
print(tree.count_leaves())

# def find_data(num):
#     for index in range(0, len(li) - 1):
#         if num != li[index]:
#             print('false')
#         else:
#             print('true')
#
# print(find_data('4'))

def is_symmetric(self, l_child, r_child):
    if l_child is None and r_child is None:
        return True
    elif l_child is None and r_child is not None:
        return False
    elif r_child is None and l_child is not None:
        return False
    elif r_child.value != l_child.value:
        return False
    else:
        return self.is_symmetric(l_child.left, r_child.right) and \
               self.is_symmetric(l_child.right, r_child.left)


def is_same(self, start1, start2):
    if start1 is None and start2 is None:
        return True
    elif start1 is None and start2 is not None:
        return False
    elif start2 is None and start1 is not None:
        return False
    elif start1.value != start2.value:
        return False
    else:
        return self.is_same(start1.left, start2.left) and \
               self.is_same(start1.right, start2.right)

