# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return head

        pointer = head
        prev = None
        while pointer.next :
            change = pointer
            pointer = pointer.next
            change.next = prev
            prev = change
        pointer.next = prev

        return pointer

        