# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root: Optional[TreeNode], low: Optional[int], high: Optional[int]):
            if not root:
                return True
            if low and root.val <= low :
                return False
            if high and root.val >= high :
                return False
            if root.left and root.left.val >= root.val :
                return False
            if root.right and root.right.val <= root.val :
                return False
            return isValid(root.left, low, root.val) and isValid(root.right, root.val, high)
        return isValid(root, None, None)
            