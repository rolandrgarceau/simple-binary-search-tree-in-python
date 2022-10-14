# BST assumes values as integers
# vscode will import for now yay!
# soon we wont have to write code anymore
# it will know what we want and do it for us! YAY!
from random import randint

PRINT = True
V_PRINT = True

class node:
    # def __init__(self, value: None) -> None:
    def __init__(self, value: None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class binary_search_tree:
    # def __init__(self) -> None:
    def __init__(self):
        # declare root on first add
        self.root = None
    # public and private functions 
    # help separate recursive calls
    def insert(self, value):
        if self.root == None:
            if PRINT:
                print(f'root set at {value}')
            self.root = node(value)
        else: # private funtion to handle
            # no longer root, we need to do checking
            self._insert(value, self.root)
    # private version
    def _insert(self, value, cur_node):
        # where to create it will happen 
        # when there is no left or right child
        if value < cur_node.value:
            # does it have a child
            if cur_node.left_child == None:
                # create one and set it
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
                if V_PRINT:
                    print(f'inserting: {value} to left_child of parent: {cur_node.left_child.parent.value}')
            else: # recursively let private _insert handle it
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value: # greater value
            if cur_node.right_child == None:
                # create one and set it
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
                if V_PRINT:
                    print(f'inserting: {value} to right_child of parent: {cur_node.right_child.parent.value}')
            else: # let private _insert handle it
                self._insert(value, cur_node.right_child)
        else: # equal to existing
            # we could create duplicates here
            if PRINT:
                print(f'found existing {value}, skipping insert')
    def p_tree(self):
        if self.root != None:
            # when does this print? Last or first?
            if PRINT or V_PRINT:
                print(f'root:{self.root.value}')# but this is a bst obj
            hite = 0 # scoped proper? use decorator
            self._p_tree(self.root, hite)
            # self._p_tree(self.root)

    def _p_tree(self, cur_node, height):
    # def _p_tree(self, cur_node,):
        # popping off in order traversal calling integers
        if cur_node != None:
            # print(f'left children:')
            height +=1
            # use _ right here
            # self._p_tree(cur_node.left_child)
            self._p_tree(cur_node.left_child, height)
            if PRINT or V_PRINT:
                print(f'_print node: {cur_node.value} at height {height}')
            # self._p_tree(cur_node.right_child)
            self._p_tree(cur_node.right_child, height)

    # recursive calls for height needs 
    # a means to store height per iteration
    # look at left and right height to leaves
    # return which ever one is greater 
    def height(self):
        # check there is a root
        if self.root != None:
            # call private method passing root
            return self._height(self.root, 0)
        else:
            return 0 # root that == None has height of zero
    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        # get rest of height from left&right subtree adding one to current height
        # compare and return highest value
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        # print(f'left_height: {left_height}')
        # print(f'right_height: {right_height}')
        return max(left_height, right_height)

    # find a value return a bool
    # use private recurive method
    # it could return the node or the value instead
    # if return node to delete it could cause problems
    def search(self, value):
        # root must be there
        if self.root != None:
            # recurse
            return self._search(value, self.root) 
        else:
            return False
    def _search(self, value, cur_node):
        # search both left and right
        # if value is in left or right return true
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child) 
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child) 
        return False # searched everywhere, no dice
    
    # helper to return node with specified input value
    # is assuming there is one to be deleted
    def find(self, value):
        if self.root != None:
            #print(f'found root')
            # start recursing with the root
            return self._find(value, self.root)
        else:
            return None
    def _find(self, value, cur_node):
        # did we find the value in current node?
        if value == cur_node.value:
            return cur_node # the node, not value here
        # if not it may be in one of its children
        elif value < cur_node.value and cur_node.left_child != None:
            self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            self._find(value, cur_node.right_child)
        # how do we get here if no value is found?
        # return False

    # delete will delete by value using delete node
    def delete_value(self, value):
        if PRINT:
            print(f'attempting to delete: {value}')
        return self.delete_node(self.find(value))
    def delete_node(self, node):
        # get to smallest left recursed value
        # staying on left children
        def min_value_node(n):
            cur = n
            if PRINT and V_PRINT:
                    print(f'going down left.child  of: {cur.value}')
            while cur.left_child != None:
                cur = cur.left_child
                if PRINT and V_PRINT:
                    print(f'currently at: {cur.value}')
            return cur
        # number of children is either 0, 1, or 2
        def num_children(n):
            num_children = 0
            if n.left_child != None: num_children +=1
            if n.right_child != None: num_children +=1
            if PRINT and V_PRINT:
                    print(f'{n.value} has {num_children}') 
            return num_children
        # get parent
        node_parent = node.parent
        # get num_children from passed in node
        node_children = num_children(node)
        # 3 match cases to handle (switch to come)
        if node_children == 0: # removes a "leaf" node
            # remove references to the node from parent
            if node_parent.left_child == node:
                if PRINT and V_PRINT:
                    print(f'leaf removing left child from parent: {node_parent.value}')
                node_parent.left_child == None
            else: # it was the right
                if PRINT and V_PRINT:
                    print(f'leaf removing right child from parent: {node_parent.value}')
                node_parent.right_child = None
                
        if node_children == 1:
            # get the correct single child node
            # we don't know which one
            # this declares a child 
            if node.left_child != None:
                child = node.left_child
            else: # it was the right
                child = node.right_child
            # swap the node to delete with its child
            if node_parent.left_child == node:
                if PRINT and V_PRINT:
                    print(f'removing {node.value} from left child of parrent {node_parent.value}')
                node_parent.left_child = child
            else:
                if PRINT and V_PRINT:
                    print(f'removing {node.value} from right child of parrent {node_parent.value}')
                node_parent.right_child = child
            # MUST indicate it went up a level in tree
            child.parent = node.parent
        if node_chilren == 2:
            # find inorder successor using min helper
            # its actually the next largest value going 
            # down the left of the right_child 
            successor = min_value_node(node.right_child)
            # get that value to the node formerly holding the value we wish to delete
            node.value = successor.value 
            # recursively delete the inorder sucessor
            # now that the value has been copied
            # to the other node
            self.delete_node(successor)
# helpers to test implementation
def fill_tree(tree, num_eles=20, max_int=100 ):
    # dont care about '_' variable use
    # # just that we iterate a fixed amount 
    for _ in range(num_eles):
        cur_ele = randint(0, max_int)
        if PRINT:
            print(f'inserting with fill_tree: {cur_ele}')
        tree.insert(cur_ele)
    return tree
# test code
bst = binary_search_tree()
# bst.p_tree() 
RANGE=10
MAX_RAND_VAL=50
if PRINT:
    print(f'filling tree with {RANGE} elements with randomly selected values between 0-{MAX_RAND_VAL}')
bst = fill_tree(bst, RANGE, MAX_RAND_VAL) # change range num_eles and max_val default
bst.p_tree() 
# my added height to print may be one off _height
# print(f'max from _height(): {bst.height()}')
# print(f'search(32): {bst.search(32)}') # True, hardcoded
# print(f'search(52): {bst.search(52)}') # False, max set to 50

