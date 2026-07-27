# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        point1 = list1
        point2 = list2

        pointer = ListNode(0, None)
        res = pointer

        while point1 and point2 :
            if point1.val <= point2.val :
                pointer.next = point1
                point1 = point1.next
            else :
                pointer.next = point2
                point2 = point2.next
            pointer = pointer.next
        
        if point1 :
            pointer.next = point1
        else :
            pointer.next = point2
        
        return res.next
            