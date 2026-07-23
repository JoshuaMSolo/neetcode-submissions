class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs :
            res += str(len(s)) + "*" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        num_beg = 0
        str_end = 0
        while i < len(s):
            if s[i] == "*" :
                str_end = i+1+int(s[num_beg : i])
                res.append(s[i+1 : str_end])
                num_beg = str_end
                i = num_beg
            i += 1
        return res