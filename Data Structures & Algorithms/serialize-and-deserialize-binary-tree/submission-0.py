# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root :
            return "##"
        else :
            left_str = self.serialize(root.left)
            right_str = self.serialize(root.right)
            return "#"+str(root.val)+"*"+str(len(left_str))+"*"+left_str+"*"+str(len(left_str))+"*"+right_str+"#"
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 2:
            return None
        else:
            i = 1
            while data[i] != "*":
                i += 1
            value = int(data[1:i])
            j = i + 1
            while data[j] != "*":
                j += 1
            left_len = int(data[i+1:j])
            left_str = data[j+1:j+1+left_len]
            i = j + 1 + left_len
            j = i + 1
            while data[j] != "*":
                j += 1
            right_len = int(data[i+1:j])
            right_str = data[j+1:-1]

            return TreeNode(value, self.deserialize(left_str), self.deserialize(right_str))

