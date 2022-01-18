import pickle

# Node object.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Python offers a a module called Pickle that lets you serialize and an object.


node = Node('root', Node('left', Node('left.left')), Node('right'))
# serialized root node.
serialized_node = pickle.dumps(node)
# deserialized root node.
deserialized_node = pickle.loads(serialized_node)
