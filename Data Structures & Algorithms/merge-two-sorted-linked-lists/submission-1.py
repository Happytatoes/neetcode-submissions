# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # idea: insert list2 nodes into list1

        answer = node = ListNode()
        curr1, curr2 = list1, list2
        
        while curr1 or curr2:
            if curr1 and not curr2:
                node.next = curr1
                break
            if curr2 and not curr1:
                node.next = curr2
                break
            if curr1.val < curr2.val:
                node.next = curr1
                node = node.next
                curr1 = curr1.next
            else:
                node.next = curr2
                node = node.next
                curr2 = curr2.next
        
        return answer.next