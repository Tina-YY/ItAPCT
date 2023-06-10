import random


class Node:
    parent = None
    left = None
    right = None
    value = None
    color = None    # black:-1, red:1

    def __init__(self, value=None, color=None, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
        self.color = color


# subtree type (enum)
class SBT:
    TRI_L = 1   # triangle left
    TRI_R = 2   # triangle right
    LIN_L = 3   # line left
    LIN_R = 4   # line right


class NC:
    BLACK = -1
    RED = 1


class RBT:
    root = None
    nil = Node(value=-1, color=NC.BLACK)

    def __init__(self, values):
        self.root = Node(values[0], NC.BLACK, self.nil, self.nil, self.nil)
        for value in values[1:]:
            self.insert(value)

    def _left_rotate(self, node):
        if node.right == self.nil:
            print("can't left rotate")
            return

        right = node.right
        parent = node.parent
        isLeft = parent.left == node

        if self.root == node:
            self.root = right

        if isLeft:
            parent.left = right
        else:
            parent.right = right
        right.parent = parent

        node.right = right.left
        right.left.parent = node

        right.left = node
        node.parent = right

    def _right_rotate(self, node):
        if node.left == self.nil:
            print("can't right rotate")
            return

        left = node.left
        parent = node.parent
        isLeft = parent.left == node

        if self.root == node:
            self.root = left

        if isLeft:
            parent.left = left
        else:
            parent.right = left
        left.parent = parent

        node.left = left.right
        left.right.parent = node

        left.right = node
        node.parent = left

    def print_tree(self):
        x_values = self._in_order_walk(self.root, [])
        y_values = self._bfs()
        x_axis = dict()
        y_axis = dict()

        for i in range(len(x_values)):
            x_axis[x_values[i]] = i
        for i in range(len(y_values)):
            for node in y_values[i]:
                y_axis[node] = i

        # 这里不能用print_matrix=[["-"*i]*j，否则因为指针关系后续更新会直接更新一整行
        print_matrix = []
        for i in range(len(y_values)):
            new_blank = []
            for j in range(len(x_values)):
                new_blank.append("-")
            print_matrix.append(new_blank)

        for node in x_axis.keys():
            print_matrix[y_axis[node]][x_axis[node]] = "{}{}({})".format(node.value, "R" if node.color==NC.RED else "B", node.parent.value)
            try:
                print_matrix[y_axis[node] - 1][x_axis[node]] = "|"
            except:
                pass

        for i in range(len(print_matrix)):
            for j in range(len(print_matrix[0])):
                print(print_matrix[i][j].center(4), end="\t")
            print("")

    def _in_order_walk(self, node, values):
        if node == self.nil:
            return values
        values = self._in_order_walk(node.left, values)
        values.append(node)
        values = self._in_order_walk(node.right, values)
        return values

    def _bfs(self):
        values = []
        nodes = [self.root]
        while len(nodes) != 0:
            new_nodes = []
            for node in nodes:
                if node.left != self.nil:
                    new_nodes.append(node.left)
                if node.right != self.nil:
                    new_nodes.append(node.right)
            values.append(nodes)
            nodes = new_nodes
        return values

    def insert(self, value):
        insert_node = Node(value, 1, None, self.nil, self.nil)
        curr_node = self.root

        while True:
            if curr_node.right == self.nil and value >= curr_node.value:
                curr_node.right = insert_node
                break
            if curr_node.left == self.nil and value <= curr_node.value:
                curr_node.left = insert_node
                break
            curr_node = curr_node.right if value >= curr_node.value else curr_node.left

        insert_node.parent = curr_node
        self._adjust(insert_node)

    def _adjust(self, node):
        # case1: node is root
        if node == self.root:
            node.color = NC.BLACK
            return

        # if node.parent is BLACK, the RBT is already valid
        # so grandparent is ALWAYS BLACK if continue processing
        if node.parent.color == NC.BLACK:
            return

        # pick up uncle, parent and grandparent(if parent is red, there must be grandparent)
        uncle, parent, grandparent, subtree_type = self._get_relative_nodes_and_subtree_type(node)

        # case2: uncle is red (implies grandparent is BLACK, parent is RED)
        if uncle.color == NC.RED:
            # change the color of uncle, parent and grand
            uncle.color = NC.BLACK
            parent.color = NC.BLACK
            grandparent.color = NC.RED
            return self._adjust(grandparent)

        # case3: uncle is black (this case includes "without uncle" cause nil node is black)
        # case3.1: deal with triangle tree type first
        if subtree_type == SBT.TRI_R:
            self._right_rotate(parent)
            subtree_type = SBT.LIN_R
            node, parent = parent, node
        if subtree_type == SBT.TRI_L:
            self._left_rotate(parent)
            subtree_type = SBT.LIN_L
            node, parent = parent, node

        # case3.2: deal with line tree type
        if subtree_type == SBT.LIN_R:
            self._left_rotate(grandparent)
        if subtree_type == SBT.LIN_L:
            self._right_rotate(grandparent)
        parent.color = NC.BLACK
        grandparent.color = NC.RED

    @staticmethod
    def _get_relative_nodes_and_subtree_type(node):
        parent = node.parent
        grandparent = parent.parent
        if parent.left == node:
            if grandparent.left == parent:
                subtree_type = SBT.LIN_L
                uncle = grandparent.right
            else:
                subtree_type = SBT.TRI_R
                uncle = grandparent.left
        else:
            if grandparent.left == parent:
                subtree_type = SBT.TRI_L
                uncle = grandparent.right
            else:
                subtree_type = SBT.LIN_R
                uncle = grandparent.left
        return uncle, parent, grandparent, subtree_type


A = [100, 14, 27, 53, 3, 25, 38, 9, 16, 23, 18, 20, 7, 12, 5, 22, 15, 94]
random.shuffle(A)
print(A)
print("=========init&insert&print test============")
rbt = RBT(A)
rbt.print_tree()
