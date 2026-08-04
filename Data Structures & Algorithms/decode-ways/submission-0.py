class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ways = [0]*(n+1)
        if s[0] == "0":
            return 0
        else :
            ways[0] = 1
            ways[1] = 1

        for i in range(2, n+1):
            if s[i-1] == "0" :
                if s[i-2] == "1" or  s[i-2] == "2":
                    ways[i] = ways[i-2]
                else :
                    return 0
            elif int(s[i-1]) <= 6 :
                if s[i-2] == "2" or s[i-2] == "1" :
                    ways[i] = ways[i-1] + ways[i-2]
                else :
                    ways[i] = ways[i-1]
            else :
                if s[i-2] == "1":
                    ways[i] = ways[i-1] + ways[i-2]
                else :
                    ways[i] = ways[i-1]

        return ways[n]
            

