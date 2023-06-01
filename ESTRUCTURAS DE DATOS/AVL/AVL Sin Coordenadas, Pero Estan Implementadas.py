from dataclasses import dataclass
from typing import Any, Union

def _minimum_node(node):
    if(node is not None):
        while(node.left is not None):
            node = node.left
        return node
    
def _maximum_node(node):
    if(node is not None):
        while(node.right is not None):
            node = node.right
        return node

#__________________________________________________________________________________AVL_________________________________________________________________________________
class Avl():

    @dataclass
    class _Node:
        key: Any
        value: Any
        height: int
        parent: Union['_Node', '_Root'] = None
        left: '_Node' = None
        right: '_Node' = None

    class _Root:
        left: '_Node' = None
        right: '_Node' = None
        parent: '_Node' = None

    __slots__ = ['_root', '_size']

    def __init__(self, key = None, value = None):
        self._root = self._Root()
        self._size = 0
        if (key is not None):
            self.insert(key, value)

    def insert(self, key, value = None):
        def do_insert(node, parent):
            if (node is None):
                node = self._Node(key, value, 1, parent)
                self._size += 1

            elif(key == node.key):
                node.value = value

            else:
                if (key < node.key):
                    node.left = do_insert(node.left, node)
                else: #key > node.key
                    node.right = do_insert(node.right, node)
                    
            node = self._balance_tree(node)
            return node
        
        self._root.left = do_insert(self._root.left, self._root)

    def _balance_tree(self, root):

        bf = self.balance_factor(root)

        if (bf == 2):
            if(self.balance_factor(root.left) == -1):
                root.left = self.rotate_left(root.left)
            root = self.rotate_right(root)
            
        elif(bf == -2):
            if(self.balance_factor(root.right)== 1):
                root.right = self.rotate_right(root.right)
            root = self.rotate_left(root)
            
        else:
            self._update_height(root)
        return root

    def balance_factor(self, node):
        factor = 0
        if (node is not None):
               
            if (node.left is not None):
                factor += node.left.height
                
            if (node.right is not None):
                factor -= node.right.height
        
            return factor

    def rotate_right(self, root):
        left_tree = root.left
        root.left = left_tree.right
        self._assing_parent(root.left, root)
        left_tree.right = root
        left_tree.parent = root.parent
        root.parent = left_tree
        root = left_tree
        self._update_height(root.right)
        self._update_height(root)
        return root

    def rotate_left(self, root):
        right_tree = root.right
        root.right = right_tree.left
        self._assing_parent(root.right, root)
        right_tree.left = root
        right_tree.parent = root.parent
        root.parent = right_tree
        root = right_tree
        self._update_height(root.left)
        self._update_height(root)
        return root

    def _assing_parent(self, node, parent):
        if (node is not None):
            node.parent = parent

    def _update_height(self, node):
        left_height = 0
        if (node.left is not None):
            left_height = node.left.height
        right_height = 0
        if (node.right is not None):
            right_height = node.right.height
        node.height = 1 + max(left_height, right_height)

    def recorrer(self):
        current = self._root.left
        self.pre_order(current)
        
    def in_order(self, current):
        if (current is not None):
            current.left = self.in_order(current.left)
            print(current.key)
            current.right = self.in_order(current.right)


#_________________________________________________________________________________Coordinate___________________________________________________________________________

    class _Coordinate():
        __slots__ = ['_node']

        def __init__(self, node = None):
            self._node = node

        @property
        def key(self):
            return self._node.key

        @property
        def value(self):
            return self._node.value

        @value.setter
        def value (self, value):
            self._node.value = value

        def advance(self):
            node = self._node
            if(node.right is not None):
                node = _minimum_node(node.right)
            else:
                while (node.parent is not None):
                    prev = node
                    node = node.parent
                    if (node.right is not prev):
                        break            
            self._node = node
            return self

        def next (self):
            return Avl._Coordinate(self._node).advance()

        def retreat(self):
            node = self._node
            if(node.left is not None):
                node = _maximum_node(node.right)
            else:
                while(node.parent is not None):
                    prev = node
                    node = node.parent
                    if (node.left is not prev):
                        break                   
            self._node = node
            return self

        def prev(self):
            return Avl._Coordinate(self._node).retreat()

        def __eq__(self, other):
            return self._node is other._node
            
