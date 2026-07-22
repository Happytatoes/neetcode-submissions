# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def invertTreeHelper(self, curr: Optional[TreeNode]):

        if not curr:
            return None

        if curr.left and curr.right:
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            self.invertTreeHelper(curr.left)
            self.invertTreeHelper(curr.right)
        elif curr.left:
            curr.right = curr.left
            curr.left = None
            self.invertTreeHelper(curr.right)
        elif curr.right:
            curr.left = curr.right
            curr.right = None
            self.invertTreeHelper(curr.left)
       
        return curr
    
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        return self.invertTreeHelper(root)
            