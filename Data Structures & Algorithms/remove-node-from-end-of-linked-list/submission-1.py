# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr:
            curr = curr.next
            size += 1

        dummy = curr = ListNode()
        dummy.next = head
        for _ in range(size - n) :
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next
        