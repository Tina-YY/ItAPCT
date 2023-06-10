class TreeNode:
    left = None
    right = None
    parent = None
    value = None

    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class BST:
    root = None

    def __init__(self, element_queue):
        self._init_tree(element_queue)

    def _init_tree(self, element_queue):
        self.root = TreeNode(element_queue[0])
        for element in element_queue[1:]:
            self.insert(element)

    def insert(self, element):
        curr_node = self.root

        while True:
            if curr_node.right is None and element >= curr_node.value:
                curr_node.right = TreeNode(element, curr_node)
                return
            if curr_node.left is None and element <= curr_node.value:
                curr_node.left = TreeNode(element, curr_node)
                return
            curr_node = curr_node.right if element >= curr_node.value else curr_node.left

    def print_tree(self):
        self._in_order_tree_walk(self.root)

    # 中序遍历
    def _in_order_tree_walk(self, node):
        if node is None:
            return
        self._in_order_tree_walk(node.left)
        print(node.value)
        self._in_order_tree_walk(node.right)

    def search(self, key):
        node = self.root
        while True:
            if node is None:
                print("no such node")
                return None
            if node.value == key:
                print("searched")
                return node
            node = node.left if key < node.value else node.right

    def maximum(self):
        node = self.root
        while node.right is not None:
            node = node.right
        print("max:", node.value)
        return node.value

    def minimum(self):
        node = self.root
        while node.left is not None:
            node = node.left
        print("min:", node.value)
        return node.value

    # return treeNode
    def successor(self, element):
        node = self.search(element)
        if node is None:
            print("no such element")
            return None
        if node.right is None:
            while node.parent is not None:
                if node == node.parent.left:
                    print("successor:", node.parent.value)
                    return node.parent
                node = node.parent
            print("biggest element already, no successor")
            return None
        node = node.right

        while node.left is not None:
            node = node.left
        print("successor:", node.value)
        return node

    def predecessor(self, element):
        node = self.search(element)
        if node is None:
            print("no such element")
            return None
        if node.left is None:
            while node.parent is not None:
                if node == node.parent.right:
                    print("predecessor:", node.parent.value)
                    return node.parent
                node = node.parent
            print("smallest element already, no predecessor")
            return None
        node = node.left

        while node.right is not None:
            node = node.right
        print("predecessor:", node.value)
        return node

    def delete(self, element):
        node = self.search(element)
        if node is None:
            print("no such element")
            return

        if node.right is None and node.left is None:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            print("deleted")
            return

        if node.right is None:
            if node == self.root:
                self.root = node.left
            elif node == node.parent.right:
                node.parent.right = node.left
                node.left.parent = node.parent
            else:
                node.parent.left = node.left
                node.left.parent = node.parent
            print("deleted")
            return
        if node.left is None:
            if node == self.root:
                self.root = node.right
            elif node == node.parent.right:
                node.parent.right = node.right
                node.right.parent = node.parent
            else:
                node.parent.left = node.right
                node.right.parent = node.parent
            print("deleted")
            return

        successor_node = self.successor(element)
        value = successor_node.value
        self.delete(value)
        node.value = value
        print("deleted")


A = [27, 53, 14, 100, 3, 25, 38, 9, 16, 23, 18, 20, 7, 12, 5, 22, 15, 94]
print("=========init&insert&print test============")
bst = BST(A)
bst.print_tree()
print("=========search test============")
bst.search(10)
bst.search(13)
print("=========max&min test============")
bst.maximum()
bst.minimum()
print("=========successor&predecessor test============")
bst.successor(100)
bst.successor(7)
bst.successor(10)
bst.predecessor(100)
bst.predecessor(18)
bst.predecessor(3)
print("=========delete test============")
bst.delete(53)
bst.print_tree()
bst.delete(27)
bst.print_tree()
bst.delete(9)
bst.print_tree()
bst.delete(22)
bst.print_tree()


