class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        n = len(nums) - 1
        if n == 1:
            return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        no_n = dp[n-1]

        dp = [0]*n
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3,n-1):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        with_n = dp[n-2]

        return max(with_n + nums[n], no_n)