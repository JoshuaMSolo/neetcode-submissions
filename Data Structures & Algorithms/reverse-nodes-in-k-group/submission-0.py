# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # idea: recursively call the function with smaller inputs
        if not head:
            return None
        
        stack = []
        i = 0
        cur = head
        while i < k and cur:
            stack.append(cur)
            cur = cur.next
            i += 1
        if len(stack) < k:
            return head

        nxt = cur
        res = cur = stack.pop()
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = self.reverseKGroup(nxt, k)

        return res