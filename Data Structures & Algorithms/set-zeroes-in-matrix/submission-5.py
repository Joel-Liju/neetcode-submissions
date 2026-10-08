class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setColToZero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == 0:
                    if matrix[i][j] == 0:
                        setColToZero = True
                    continue
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][0] == 0:
                matrix[0][j] = 0
        for i in range(len(matrix)):
            if setColToZero:
                matrix[i][0] = 0