class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # helper to search for word[word_i:], starting from board[i][j]
        def search(i, j, word_i) :
            if board[i][j] != word[word_i]:
                return False
            if word_i == len(word)-1 :
                return True
            else :
                char = board[i][j]
                board[i][j] = "*"
                for row, col in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= row < len(board) and 0 <= col < len(board[0]):
                        if search(row, col, word_i+1):
                            return True
                board[i][j] = char
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i,j,0):
                    return True
        return False        