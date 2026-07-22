class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            d = defaultdict(int)
            for c in str :
                d[c] += 1
            d_list = []
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            for i in range(26) :
                d_list.append(d[alphabet[i]])
            groups[tuple(d_list)].append(str)
        
        return list(groups.values())



        