class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        self.path = []
        self.res = []
        def dfs(target, latestIdx) :
            for i in range(latestIdx, n):
                if nums[i] > target:
                    continue
                elif nums[i] == target:
                    self.res.append(self.path + [nums[i]])
                else :
                    tmp = self.path.copy()
                    self.path += [nums[i]]
                    dfs(target - nums[i], i)
                    self.path = tmp.copy()
        
        dfs(target, 0)
        return self.res
