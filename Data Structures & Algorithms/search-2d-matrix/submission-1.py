class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        # invariant : matrix[t][0] <= target <= matrix[b+1][0]
        while t < b:
            m = (t + b + 1) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                b = m - 1
            else :
                t = m
        # t = b = row where target must be in
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[t][m] == target:
                return True
            elif matrix[t][m] > target:
                r = m - 1
            else :
                l = m + 1
        
        return False