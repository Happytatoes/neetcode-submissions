"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(old):
            if old in old_to_new:
                return old_to_new[old] 

            # create new node
            new = Node(old.val)
            old_to_new[old] = new
            # add neighbors   
            for neighbor in old.neighbors:
                new.neighbors.append(dfs(neighbor))
            return new
            
        return dfs(node)






