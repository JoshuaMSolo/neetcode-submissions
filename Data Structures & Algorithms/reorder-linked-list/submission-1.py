# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        while head.next :
            if not head.next.next :
                break
            new_end = head
            while new_end.next.next :
                new_end = new_end.next
            end = new_end.next
            new_end.next = None
            end.next = head.next
            head.next = end
            head = end.next

            
        