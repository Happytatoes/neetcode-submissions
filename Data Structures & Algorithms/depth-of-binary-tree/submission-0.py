# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, curr: Optional[TreeNode]):
        
        res = 0

        if not curr:
            return 0
        
        if curr.left and curr.right:
            return 1 + max(self.helper(curr.left), self.helper(curr.right))
        elif curr.left:
            return 1 + self.helper(curr.left)
        elif curr.right: 
            return 1 + self.helper(curr.right)
        else:
            return 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)