class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        while (not s[i].isalnum()) and (i < len(s)-1) :
            i += 1
        j = len(s)-1
        while (not s[j].isalnum()) and (j > 0) :
            j -= 1

        while i<j :
            if s[i].lower() != s[j].lower() :
                return False
            else :
                i += 1
                while not s[i].isalnum() :
                    i += 1
                j -= 1
                while not s[j].isalnum() :
                    j -= 1

        return True