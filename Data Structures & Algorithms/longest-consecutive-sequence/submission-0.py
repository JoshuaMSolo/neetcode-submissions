class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = {}
        starter = {}
        for num in nums :
            num_set[num] = True

        for num in num_set :
            if num - 1 not in num_set :
                starter[num] = True
        
        res = 0
        for num in starter :
            this_res = 1
            while num + 1 in num_set :
                this_res += 1
                num += 1
            res = max(res, this_res)
        
        return res