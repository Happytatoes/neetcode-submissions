# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = 0, 0

        curr, value = l1, 0
        while curr:
            first += curr.val * (10 ** value)
            value += 1
            curr = curr.next
        
        curr, value = l2, 0
        while curr:
            second += curr.val * (10 ** value)
            value += 1
            curr = curr.next
        
        ans = str(first + second)
        digits = len(ans)
        curr = ListNode()
        dummy = curr
        
        while digits > 0:  
            num = ans[digits - 1]
            curr.next = ListNode(num)
            curr = curr.next
            digits -= 1
        
        return dummy.next
        
        
