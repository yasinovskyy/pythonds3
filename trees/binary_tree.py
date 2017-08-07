'''
Bradley N. Miller, David L. Ranum
Introduction to Data Structures and Algorithms in Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''

import operator


class BinaryTree:
    '''
    A recursive implementation of Binary Tree
    Using links and Nodes approach.

    Modified to allow for trees to be constructed from other trees
    rather than always creating a new tree in the insert_feft or insert_right
    '''

    def __init__(self, root_obj):
        '''Create new tree'''
        self.__key = root_obj
        self.__child_left = None
        self.__child_right = None

    def get_root_val(self):
        '''Get root key value'''
        return self.__key

    def set_root_val(self, root_obj):
        '''Set root key value'''
        self.__key = root_obj

    def get_child_left(self):
        '''Get left child'''
        return self.__child_left

    def set_child_left(self, new_child_left):
        '''Set left child'''
        self.__child_left = new_child_left

    def get_child_right(self):
        '''Get right child'''
        return self.__child_right

    def set_child_right(self, new_child_right):
        '''Set right child'''
        self.__child_right = new_child_right

    def is_leaf(self):
        '''Check if a node is leaf'''
        return (not self.__child_left) and (not self.__child_right)

    def insert_left(self, new_node):
        '''Insert left subtree'''
        if isinstance(new_node, BinaryTree):
            new_subtree = new_node
        else:
            new_subtree = BinaryTree(new_node)

        if self.__child_left:
            new_subtree.set_child_left(self.__child_left)

        self.__child_left = new_subtree

    def insert_right(self, new_node):
        '''Insert right subtree'''
        if isinstance(new_node, BinaryTree):
            new_subtree = new_node
        else:
            new_subtree = BinaryTree(new_node)

        if self.__child_right:
            new_subtree.set_child_right(self.__child_right)
        self.__child_right = new_subtree

    def preorder(self):
        '''Pre-order tree traversal'''
        print(self.__key, end=' ')
        if self.__child_left:
            self.__child_left.preorder()
        if self.__child_right:
            self.__child_right.preorder()

    def inorder(self):
        '''In-order tree traversal'''
        if self.__child_left:
            self.__child_left.inorder()
        print(self.__key, end=' ')
        if self.__child_right:
            self.__child_right.inorder()

    def postorder(self):
        '''Post-order tree traversal'''
        if self.__child_left:
            self.__child_left.postorder()
        if self.__child_right:
            self.__child_right.postorder()
        print(self.__key, end=' ')

    def print_exp(self):
        '''Print an expression'''
        if self.__child_left:
            print('(', end=' ')
            self.__child_left.print_exp()
        print(self.__key, end=' ')
        if self.__child_right:
            self.__child_right.print_exp()
            print(')', end=' ')

    def postorder_eval(self):
        '''Postorder evaluation'''
        operations = {'+': operator.add,
                      '-': operator.sub,
                      '*': operator.mul,
                      '/': operator.truediv}
        res1 = None
        res2 = None
        if self.__child_left:
            res1 = self.__child_left.postorder_eval()  # \label{peleft}
        if self.__child_right:
            res2 = self.__child_right.postorder_eval()  # \label{peright}
        if res1 and res2:
            return operations[self.__key](res1, res2)  # \label{peeval}
        else:
            return self.__key

    def height(self):
        '''Height of a tree'''
        if not self.__key:
            return -1
        if self.__child_left:
            height_left = self.__child_left.height()
        else:
            height_left = -1

        if self.__child_right:
            height_right = self.__child_right.height()
        else:
            height_right = -1

        return 1 + max(height_left, height_right)

    def count_nodes(self):
        '''Count nodes in a tree'''
        if not self.__key:
            return 0
        if self.__child_left:
            children_left = self.__child_left.count_nodes()
        else:
            children_left = 0

        if self.__child_right:
            children_right = self.__child_right.count_nodes()
        else:
            children_right = 0

        return 1 + children_left + children_right