# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find beginning of second half
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second_half_head = slow.next

        # reverse the second half
        prev = None
        curr = second_half_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        end = prev

        # cut off first half from second half nodes
        slow.next = None

        # interleave coming from head and tail 
        start = head
        while end and start: 
            start_next, end_next = start.next, end.next
            start.next = end
            end.next = start_next
            start, end = start_next, end_next
           


    