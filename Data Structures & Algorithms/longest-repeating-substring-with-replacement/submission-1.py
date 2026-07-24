class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        left = 0
        longest = 0

        def invalid(dic : dict[str,int], length : int) -> bool :
            for value in dic.values() :
                if value + k >= length :
                    return False
            return True

        for right in range(len(s)) :
            d[s[right]] += 1
            while invalid(d, right-left+1) :
                d[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest