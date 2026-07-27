# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p :
                if not q :
                    return False
                else :
                    if p.val != q.val :
                        return False
                    else :
                        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else :
                if q :
                    return False
                else :
                    return True
        
        if isSameTree(root, subRoot) :
            return True
        elif not root :
            return not subRoot
        else :
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)