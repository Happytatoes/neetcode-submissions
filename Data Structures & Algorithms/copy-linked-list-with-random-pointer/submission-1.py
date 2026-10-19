"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        old_to_new = {}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        for old in old_to_new:
            new = old_to_new[old]
            if not old.next:
                new.next = None
            else:
                new.next = old_to_new[old.next]
            if not old.random:
                new.random = None
            else:
                new.random = old_to_new[old.random]
        

        return old_to_new[head]