# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        pointer = dummy

        minHeap = []
        for index, n in enumerate(lists) :
            minHeap.append((n.val, index, n))
        
        heapq.heapify(minHeap)

        while minHeap :
            value, index, next_node = heapq.heappop(minHeap)
            pointer.next = next_node
            pointer = pointer.next
            if next_node.next :
                heapq.heappush(minHeap, (next_node.next.val, index, next_node.next))
        
        return dummy.next
            
