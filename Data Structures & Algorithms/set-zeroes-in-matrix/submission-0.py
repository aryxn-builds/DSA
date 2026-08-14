class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = [1] * len(matrix)
        col = [1] * len(matrix[0])

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row[r] = 0
                    col[c] = 0
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if row[r] == 0 or col[c] == 0:
                    matrix[r][c] = 0