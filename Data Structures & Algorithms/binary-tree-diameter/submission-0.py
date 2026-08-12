# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, curr: Optional[TreeNode]):
        
        if curr == None or not (curr.left or curr.right):
            return 0

        elif curr.left and (not curr.right):
            return 1 + self.helper(curr.left)
        
        elif curr.right and (not curr.left):
            return 1 + self.helper(curr.right)

        else:
            return 1 + max(self.helper(curr.left), self.helper(curr.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        left = 1 + self.helper(root.left) if root.left else 0
        right = 1 + self.helper(root.right) if root.right else 0
        
        return max(left + right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        