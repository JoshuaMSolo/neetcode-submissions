class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            res = []
            for sset in self.subsets(nums[1:]):
                res.append(sset)
                res.append([nums[0]]+sset)
            return res