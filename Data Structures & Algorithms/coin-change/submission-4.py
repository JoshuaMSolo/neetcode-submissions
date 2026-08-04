class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :
            return 0
        min_coins : List[Optional[int]] = [None]*(amount+1)
        min_coins[0] = 0
        for i in range(1, amount+1) :
            min_now : Optional[int] = None
            for coin in coins:
                if i >= coin and min_coins[i-coin] is not None:
                    if min_now is not None:
                        min_now = min(min_now, min_coins[i-coin] + 1)
                    else :
                        min_now = min_coins[i-coin] + 1
            min_coins[i] = min_now

        return min_coins[amount] if min_coins[amount] else -1