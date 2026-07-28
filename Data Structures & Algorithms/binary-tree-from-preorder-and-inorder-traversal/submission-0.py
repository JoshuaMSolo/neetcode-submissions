# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        size = len(preorder)
        
        if size == 0 :
            return None
        elif size == 1 :
            return TreeNode(preorder[0], None, None)

        left_count = 0
        root_val = preorder[0]
        for num in inorder :
            if num != root_val :
                left_count += 1
            else :
                break
        # left_count is the size of the left subtree

        left_subtree = self.buildTree(preorder[1:1+left_count], inorder[0:left_count])
        right_subtree = self.buildTree(preorder[left_count+1:], inorder[left_count+1:])
        return TreeNode(root_val, left_subtree, right_subtree)