class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(len(temperatures)):
            t = temperatures[i]
            if not stack :
                stack.append((temperatures[i], i))
            else :
                while stack and t > stack[-1][0]:
                    ind = stack.pop()[1]
                    res[ind] = i - ind
                stack.append((temperatures[i], i))
        
        return res
