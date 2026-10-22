# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.i = k
        self.res = 0

        def dfs(node):
            if node:
                dfs(node.left)
                self.i -= 1
                if self.i == 0:
                    self.res = node.val
                dfs(node.right)
        
        dfs(root)
        return self.res    