class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        toAfter = {}
        toBefore = {}
        # invariant : a in toAfter[b] if and ony if b in toBefore[a]
        for p in prerequisites :
            if p[1] not in toAfter.setdefault(p[0], set()) :
                toAfter.setdefault(p[1], set()).add(p[0])
                toBefore.setdefault(p[0], set()).add(p[1])
                for course in toAfter.setdefault(p[0], set()) :
                    if p[1] in toAfter[course] :
                        return False
                    else :
                        toAfter[p[1]].add(course)
                        toBefore[course].add(p[1])
                for course in toBefore.setdefault(p[1], set()) :
                    if p[0] in toBefore[course] :
                        return False
                    else :
                        toBefore[p[0]].add(course)
                        toAfter[course].add(p[0])
            else :
                return False
        
        return True