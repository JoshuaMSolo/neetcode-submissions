# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0

            leftrad = dfs(node.left)+1 if node.left else 0
            rightrad = dfs(node.right)+1 if node.right else 0
            self.res = max(self.res, (leftrad) + (rightrad))

            return max(leftrad, rightrad)
        
        dfs(root)
        return self.res