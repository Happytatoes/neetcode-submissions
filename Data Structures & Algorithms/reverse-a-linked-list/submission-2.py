# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        if not head.next:
            return head

        c = head
        n = c.next
        c.next = None

        while n.next:
            nn = n.next
            n.next = c
            c = n
            n = nn
        
        n.next = c

        return n