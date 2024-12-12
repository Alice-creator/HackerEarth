class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def right_rotate(self, node):
        temp = node
        temp.left = node.left.right
        
        node = node.left
        node.right = temp

        temp.height = max(temp.left.height, temp.right.height) + 1
        node.height = max(node.left.height, node.right.height) + 1

        return node

    def left_rotate(self, node):
        temp = node
        temp.right = node.right.left
        
        node = node.right
        node.left = temp

        temp.height = max(temp.right.height, temp.left.height) + 1
        node.height = max(node.right.height, node.left.height) + 1

        return node

    def get_bf(self, node):
        left = node.left.height if node.left != None else 0
        right = node.right.height if node.right != None else 0
        return left - right

    def insert(self, node, value):
        if self.node == None:
            return Node(value)
        elif self.node.value < value:
            self.node.right = self.insert(self.node.right, value)
        elif self.node.value > value:
            self.node.left = self.insert(self.left, value)
        
        node.height = max(node.left.height, node.right.height) + 1

        balance_factor = self.get_bf(node)

        if balance_factor > 1:
            if value > node.left.value:
                node.left = self.left_rotate(node.left)
            node = self.right_rotate(node)
        elif balance_factor < 1:
            if value < node.right.value:
                node.right = self.right_rotate(node.right)
            node = self.left_rotate(node)
        
        return node