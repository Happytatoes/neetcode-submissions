# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr):
            if curr == None:
                return 0
            else:
                if abs(dfs(curr.left) - dfs(curr.right)) > 1:
                    self.balanced = False
                return 1 + max(dfs(curr.left), dfs(curr.right))
        
        dfs(root)

        return self.balanced







