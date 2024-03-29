# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        def ismirror(left, right):
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            else:
                return left.val == right.val and ismirror(left.left, right.right) and ismirror(left.right, right.left)

        if root == None:
            return True
        else:
            return ismirror(root, root)
