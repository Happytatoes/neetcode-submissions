# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, curr: TreeNode, p: TreeNode, q: TreeNode):

        print (p.val)
        print (curr.val)
        print (q.val)

        print (p.val <= curr.val)
        print (q.val >= curr.val)

        if (p.val <= curr.val and q.val >= curr.val) or (p.val >= curr.val and q.val <= curr.val):
            return curr
        
        elif (not curr.left) and curr.right:
            return self.helper(curr.right, p, q)

        elif (not curr.right) and curr.left:
            return self.helper(curr.left, p, q)

        else:
            if p.val > curr.val and q.val > curr.val:
                return self.helper(curr.right, p, q)
            elif q.val < curr.val and p.val < curr.val:
                return self.helper(curr.left, p, q)
        
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.helper(root, p, q)



