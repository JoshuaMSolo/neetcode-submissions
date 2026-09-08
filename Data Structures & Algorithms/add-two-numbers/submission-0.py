# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            cur.next = ListNode(0)
            cur = cur.next
            curval = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if curval > 9:
                carry = 1
                cur.val = curval - 10
            else:
                carry = 0
                cur.val = curval
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        return res.next