class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d_pos = defaultdict(list)
        d_neg = defaultdict(list)
        for i in range(len(nums)) :
            if nums[i] >= 0 :
                d_pos[nums[i]].append(i)
            else :
                d_neg[- nums[i]].append(i)
        res = []
        skip = set()
        for ni in d_pos :
            skip.clear()
            for nj in d_neg :
                if ni <= nj or nj in skip:
                    continue
                target = ni - nj
                if target in d_neg :
                    if target != nj :
                        res.append([ni, - nj, - target])
                        skip.add(target)
                    else :
                        if len(d_neg[target]) > 1 :
                            res.append([ni,-nj,-target])
                            skip.add(target)

        for ni in d_neg :
            skip.clear()
            for nj in d_pos :
                if ni < nj or nj in skip:
                    continue
                target = ni - nj
                if target in d_pos :
                    if target != nj :
                        res.append([-ni,nj,target])
                        skip.add(target)
                    else :
                        if len(d_pos[target]) > 1 :
                            res.append([-ni,nj,target])
                            skip.add(target)

        if len(d_pos[0]) >= 3:
            res.append([0,0,0])
        
        return res
