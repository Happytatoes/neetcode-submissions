# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]):
        if (not a) and (not b):
            return True
        elif a and not b:
            return False
        elif a.val != b.val:
            return False

        if (not a.left and b.left) or (a.left and not b.left):
            return False
        if (not a.right and b.right) or (a.right and not b.right):
            return False
        
        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)

    def isSubTreeHelper(self, curr: Optional[TreeNode], subRoot: Optional[TreeNode]):

        if self.isSameTree(curr, subRoot):
            return True
        
        if curr.left:
            if self.isSubTreeHelper(curr.left, subRoot):
                return True
        if curr.right:
            if self.isSubTreeHelper(curr.right, subRoot):
                return True

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubTreeHelper(root, subRoot)





