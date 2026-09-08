"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ori_to_copy = {}
        
        if not head:
            return None
            
        head_copy = Node(head.val, None, None)
        ori_to_copy[head] = head_copy

        point = head
        point_copy = head_copy
        while point.next:
            nex = Node(point.next.val, None, None)
            point_copy.next = nex
            point = point.next
            point_copy = point_copy.next
            ori_to_copy[point] = point_copy

        point = head
        point_copy = head_copy
        while point:
            if point.random:
                point_copy.random = ori_to_copy[point.random]
            else:
                point_copy.random = None
            point = point.next
            point_copy = point_copy.next

        return head_copy
