import sys
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            return self.right.contains(target) if self.right else False
        else:
            return self.left.contains(target) if self.left else False

    # Return the maximum value found in the tree
    def get_max(self):
        def get_max_recursion(node):
            if node.right is None:
                return node.value
            else:
                return get_max_recursion(node.right)
        return get_max_recursion(self)

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        self.left and self.left.for_each(cb)
        self.right and self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.left and self.in_order_print(node.left)
        print(node.value)
        node.right and self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            dequeued = queue.dequeue()
            print(dequeued.value)
            dequeued.left and queue.enqueue(dequeued.left)
            dequeued.right and queue.enqueue(dequeued.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            current_node = stack.pop()
            print(current_node.value)
            current_node.left and stack.push(current_node.left)
            current_node.right and stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
