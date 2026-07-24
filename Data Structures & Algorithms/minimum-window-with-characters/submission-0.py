class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        surplus = {}
        for c in t :
            d[c] = d.setdefault(c,0) + 1
        
        left = 0
        shortest = len(s)

        for right in range(len(s)) :
            if s[right] in d :
                if d[s[right]] == 1 :
                    del d[s[right]]
                    surplus[s[right]] = 0
                else :
                    d[s[right]] -= 1
            elif s[right] in surplus :
                surplus[s[right]] += 1
            
            if d :
                if right == len(s) - 1:
                    return ""
                continue
            else :
                while s[left] not in surplus or surplus[s[left]] > 0 :
                    if s[left] in surplus :
                        surplus[s[left]] -= 1
                    left += 1
                if right - left + 1 <= shortest :
                    temp = (left,right+1)
                    shortest = right-left+1
        
        return s[temp[0]:temp[1]]