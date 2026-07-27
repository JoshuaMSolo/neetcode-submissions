# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_last = []
        cur = head
        while cur :
            if len(n_last) < n + 1 :
                n_last.append(cur)
            else :
                n_last = n_last[1:] + [cur]
            cur = cur.next
        
        if len(n_last) == n :
            return head.next
        else :
            point = n_last[0]
            point.next = point.next.next
            return head