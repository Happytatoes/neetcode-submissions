# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        
        if (not p) and (not q):
            return True
        elif (not p) or (not q):
            return False

        if p.val != q.val:
            return False
        
        if p.left and q.left:
            if not self.helper(p.left, q.left):
                return False
        elif p.left or q.left:
            return False

        if p.right and q.right:
            if not self.helper(p.right, q.right):
                return False
        elif p.right or q.right:
            return False
        
        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)
