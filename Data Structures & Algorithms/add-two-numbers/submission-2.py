# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry == 1:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2: 
                num += l2.val
                l2 = l2.next
            num += carry
            carry = num // 10
            num = num % 10
            new = ListNode()
            new.val = num
            curr.next = new
            curr = curr.next
        
        return dummy.next
