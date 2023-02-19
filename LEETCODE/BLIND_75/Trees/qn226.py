# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        #swap the children
        temp = root.right
        root.right = root.left
        root.left = temp

        #recursive for left subtree
        self.invertTree(root.left)
        #recursive for right subtree
        self.invertTree(root.right)
        return root
                