# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        d = {}

        def size(root: Optional[TreeNode]) -> int :
            if not root :
                d[root] = 0
            else :
                d[root] = 1 + size(root.left) + size(root.right)
            return d[root]

        size(root)

        while root :
            size_left = d[root.left]
            if size_left == k - 1 :
                return root.val
            elif size_left >= k :
                root = root.left
            else :
                root = root.right
                k -= 1 + size_left

        