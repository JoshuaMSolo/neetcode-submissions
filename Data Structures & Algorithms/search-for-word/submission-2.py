class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])

        def search(word: str,i: int, j: int, board: List[List[str]], visited: set):
            if board[i][j] == word[0] :
                if len(word) == 1 :
                    return True
                else :
                    for row, column in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                        if row < num_rows and row >= 0 and column < num_cols and column >= 0 and (row,column) not in visited:
                            visited_new = visited.copy()
                            visited_new.add((row,column))
                            if search(word[1:], row, column, board, visited_new) :
                                return True
            else :
                return False

        for i in range(num_rows) :
            for j in range(num_cols) :
                if board[i][j] == word[0] :
                    if search(word, i, j, board, set([(i,j)])) :
                        return True
        return False
    
