"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        
        def cloneNode(node) :
            if not node :
                return None
            elif node in clones :
                return clones[node]
            else :
                new_node = Node(node.val, [])
                clones[node] = new_node
                for neighbor in node.neighbors :
                    new_node.neighbors.append(cloneNode(neighbor))
                return new_node
        
        return cloneNode(node)