# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, curmax):
            nonlocal res

            if not node:
                return

            if curmax <= node.val:
                res += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, curmax)
                dfs(node.right, curmax)
        
        dfs(root, -101)
        return res