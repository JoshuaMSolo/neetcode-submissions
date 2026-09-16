class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        else:
            res = []
            num = nums[0]
            for perm in self.permute(nums[1:]):
                for i in range(len(nums)):
                    res.append(perm[:i] + [num] + perm[i:])
            return res