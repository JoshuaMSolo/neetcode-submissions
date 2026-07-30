class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        toRep = {i : i for i in range(n)}
        def findRep(i) :
            if toRep[i] == i:
                return i
            else :
                toRep[i] = findRep(toRep[i])
                return toRep[i]
        
        if len(edges) != n-1 :
            return False
        else :
            for a, b in edges:
                a_rep, b_rep = findRep(a), findRep(b)
                if a_rep == b_rep :
                    return False
                toRep[b_rep] = a_rep
            return True
        
        
