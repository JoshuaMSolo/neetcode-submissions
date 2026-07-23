class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        pref_min = prices[0]
        profit = 0
        while i < len(prices) :
            profit = max(profit, prices[i] - pref_min)
            pref_min = min(pref_min, prices[i])
            i += 1
        return profit