class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        if len(s2) < window_len:
            return False
        
        check = [0] * 26
        window = [0] * 26
        for i in range(window_len):
            check[ord(s1[i])-97] += 1
            window[ord(s2[i])-97] += 1
        
        for i in range(len(s2) - window_len):
            if check == window:
                return True
            else:
                window[ord(s2[i])-97] -= 1
                window[ord(s2[i+window_len])-97] += 1

        return check == window
        