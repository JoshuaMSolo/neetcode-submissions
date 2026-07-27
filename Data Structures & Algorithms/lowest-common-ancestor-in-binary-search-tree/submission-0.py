# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_list = [root]
        q_set = set([root])
        
        node = root
        while node.val != p.val :
            if p.val < node.val :
                node = node.left
            else :
                node = node.right
            p_list.append(node)
        node = root
        while node.val != q.val :
            if q.val < node.val :
                node = node.left
            else :
                node = node.right
            q_set.add(node)
        
        for i in range(len(p_list)-1, -1, -1):
            if p_list[i] in q_set:
                return p_list[i]