class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def mark(row: int, col: int, grid: List[List[str]]) :
            grid[row][col] = "0"
            for neighbor in [(row+1, col), (row-1,col), (row,col+1), (row,col-1)]:
                a = neighbor[0]
                b = neighbor[1]
                if a < m and a >= 0 and b < n and b >= 0 and grid[a][b] == "1":
                    mark(a,b,grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" :
                    mark(i, j, grid)
                    count += 1
        
        return count