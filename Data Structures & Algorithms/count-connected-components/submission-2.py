class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        toRep = [i for i in range(n)]

        def findRep(i) :
            if toRep[i] != i:
                toRep[i] = findRep(toRep[i])
            return toRep[i]

        res = n
        for a, b in edges :
            a_rep, b_rep = findRep(a), findRep(b)
            if a_rep != b_rep:
                res -= 1
                toRep[b_rep] = a_rep
        
        return res
