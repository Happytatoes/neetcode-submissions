# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    largest_diam = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # returns height, 
        # stores current max val in largest_diam if its greater
        def dfs(curr):
            if not curr:
                return 0
            if curr: 
                if not (curr.left or curr.right):
                    return 0
                else: 
                    l = 1 + dfs(curr.left) if curr.left else dfs(curr.left)
                    r = 1 + dfs(curr.right) if curr.right else dfs(curr.right)
                    self.largest_diam = max(self.largest_diam, (l + r)) 
                    return 1 + max(dfs(curr.left), dfs(curr.right))
        
        dfs(root)
        return self.largest_diam
            














