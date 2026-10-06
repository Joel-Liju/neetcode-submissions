import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(math.ceil(len(matrix)/2)):
            j = i
            loc = len(matrix) - i - 1
            
            temp = matrix[i][loc]
            matrix[i][loc] = matrix[i][j]
            
            temp2 = matrix[loc][loc]
            matrix[loc][loc] = temp
            temp = temp2

            temp2 = matrix[loc][i]
            matrix[loc][i] = temp
            temp = temp2

            matrix[i][j] = temp
            
            j += 1
            while j < len(matrix) - (i + 1):
                
                temp = matrix[j][loc]
                matrix[j][loc] = matrix[i][j]

                temp2 = matrix[loc][len(matrix) - j - 1]
                matrix[loc][len(matrix) - j - 1] = temp
                temp = temp2

                temp2 = matrix[len(matrix) - j - 1][i]
                matrix[len(matrix) - j - 1][i] = temp
                temp = temp2

                matrix[i][j] = temp
                
                j += 1