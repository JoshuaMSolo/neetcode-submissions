class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {}
        for i in range(9):
            d["row" + str(i)] = [False] * 9
            d["col" + str(i)] = [False] * 9
            d["box" + str(i)] = [False] * 9
        
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == "." :
                    continue
                else :
                    c = int(c) - 1
                row = "row" + str(i)
                col = "col" + str(j)
                box = "box" + str(3 * (i//3) + j//3)
                for group in [row, col, box]:
                    if d[group][c] :
                        return False
                    d[group][c] = True
                
        return True