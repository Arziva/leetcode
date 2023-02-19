class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))