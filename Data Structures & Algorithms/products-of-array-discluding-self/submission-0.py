class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]
        suffix_prod = [1]
        n = len(nums)
        prod = 1
        for i in range(n-1) :
            prod *= nums[i]
            prefix_prod.append(prod)
        prod = 1
        for i in range(n-1, 0, -1):
            prod *= nums[i]
            suffix_prod.append(prod)
        
        res = []
        for i in range(n) :
            res.append(prefix_prod[i] * suffix_prod[n-i-1])

        return res