# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = curr = ListNode()
        carry = 0

        while l1 or l2 or carry == 1:
            num_1 = l1.val if l1 else 0
            num_2 = l2.val if l2 else 0 
            num = num_1 + num_2 + carry
            carry = 0

            if num >= 10:
                num = num % 10
                carry = 1

            curr.next = ListNode(num)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        
        
