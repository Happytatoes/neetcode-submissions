# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        supertrailer = head
        trailer = head
        leader = head

        for _ in range(n):
            leader = leader.next
        
        while leader:
            leader = leader.next
            old = trailer
            trailer = trailer.next
            supertrailer = old
        
        if trailer == head:
            return trailer.next
        
        supertrailer.next = supertrailer.next.next
        return head