class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        for pile in piles:
            if pile > k:
                k = pile
        l, r, = 1, k
        while l < r:
            m = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)

            if hours > h:
                l = m+1
            else:
                r = m
        return l
