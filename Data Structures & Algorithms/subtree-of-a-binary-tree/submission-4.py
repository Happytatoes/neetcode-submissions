# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False

        if p.val != q.val:
            return False
        if (not self.isSameTree(p.left, q.left)) or (not self.isSameTree(p.right, q.right)):
            return False
        
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if self.isSameTree(root, subRoot):
            return True
        if root.left:
            if self.isSubtree(root.left, subRoot):
                return True
        if root.right:
            if self.isSubtree(root.right, subRoot):
                return True
        return False 


       





