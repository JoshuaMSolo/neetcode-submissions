class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        left = 0
        longest = 0
        max_freq = 0

        for right in range(len(s)) :
            d[s[right]] += 1
            max_freq = max(max_freq, d[s[right]])

            if right - left + 1 - max_freq > k :
                d[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        return longest