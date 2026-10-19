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
        
        # The old version, we needed to check if next, random, and head
        # were none each time since it would throw a key error
        # every time we tried to access old_to_new[old.next] 
        # or old_to_new[old.random]
        # but what we can do instead is this... now, if we try to access
        # old_to_new[None] we get None
        
        old_to_new = {None: None}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head
        while curr:
            new = old_to_new[curr]
            new.next = old_to_new[curr.next]
            new.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]