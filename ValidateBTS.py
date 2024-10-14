"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees."""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        array = []
        array = inorder(root, array)
        sortArray = sorted(array)

        if containsDuplicate(array):
            return False
        
        return array == sortArray



def inorder(curr, l): #In order traversal helper!
    if curr.left != None:
        inorder(curr.left, l)

    l.append(curr.val)

    if curr.right != None:
        inorder(curr.right, l)

    return l

def containsDuplicate(array): #checks if a tree has duplicates which shouldnt happen!
    s = set(array)
    return len(s) != len(array)

        