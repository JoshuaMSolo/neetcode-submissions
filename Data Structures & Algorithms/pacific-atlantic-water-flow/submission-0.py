class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        toPacific = set()
        toAtlantic = set()
        
        def dfsPac(r, c) :
            toPacific.add((r,c))
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] :
                if 0 <= next_r < n and 0 <= next_c < m and (next_r, next_c) not in toPacific :
                    if heights[next_r][next_c] >= heights[r][c] or next_r == 0 or next_c == 0:
                        dfsPac(next_r, next_c)

        def dfsAtl(r,c) :
            toAtlantic.add((r,c))
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] :
                if 0 <= next_r < n and 0 <= next_c < m and (next_r, next_c) not in toAtlantic:
                    if heights[next_r][next_c] >= heights[r][c] or next_r == n - 1 or next_c == m - 1:
                        dfsAtl(next_r, next_c)

        dfsPac(0,0)
        dfsAtl(n-1,m-1)
        res = []
        for cell in toPacific :
            if cell in toAtlantic :
                res.append(cell)

        return res