class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        tot = 0
        res = 0
        maxim = -1
        max_ind = n
        between = 0

        for i in range(n-1, -1, -1):
            if height[i] >= maxim:
                res += (max_ind - i - 1) * maxim - between
                maxim = height[i]
                max_ind = i
                between = 0
            else:
                between += height[i]
        
        maxi = max_ind
        maxim = -1
        max_ind = -1
        between = 0
        for i in range(maxi + 1):
            if height[i] >= maxim:
                res += (i - max_ind - 1) * maxim - between
                maxim = height[i]
                max_ind = i
                between = 0
            else :
                between += height[i]

        return res