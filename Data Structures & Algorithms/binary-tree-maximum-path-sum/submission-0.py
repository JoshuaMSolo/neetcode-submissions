# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_from_node = {}
        def maxFromNode(node: Optional[TreeNode]) -> int :
            if not node :
                return 0
            return max_from_node.setdefault(node, node.val + max([maxFromNode(node.left), maxFromNode(node.right),0]))
        
        max_sum = maxFromNode(root)
        for key in max_from_node :
            max_sum = max(max_sum, max(maxFromNode(key), key.val + maxFromNode(key.left) + maxFromNode(key.right)))

        return max_sum