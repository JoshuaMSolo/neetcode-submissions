# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        queue = deque([root])
        res = []
        node_in_level = 1
        while len(queue) > 0:
            temp = []
            next_level = 0
            for i in range(node_in_level) :
                if len(queue) > 0:
                    node = queue.popleft()
                    if node:
                        temp.append(node.val)
                        if node.left :
                            queue.append(node.left)
                            next_level += 1
                        if node.right :
                            queue.append(node.right)
                            next_level += 1
            res.append(temp)
            node_in_level = next_level
        return res

