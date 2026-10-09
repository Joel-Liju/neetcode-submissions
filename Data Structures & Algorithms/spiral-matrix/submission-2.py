import math
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        returnList = []
        for r in range(min(math.ceil(len(matrix[0])/2),math.ceil(len(matrix)/2))):
            i,j = r, r
            for t in range(4):
                if t == 0:
                    while j < len(matrix[r]) - r:
                        returnList.append(matrix[i][j])
                        j += 1
                elif t == 1:
                    j -= 1
                    i += 1
                    if i >= len(matrix) - r:
                        break
                    while i < len(matrix) - r:
                        print(i,j,r)
                        returnList.append(matrix[i][j])
                        i += 1
                elif t == 2:
                    i -= 1
                    j -= 1
                    if j <= r - 1:
                        break
                    while j > r - 1:
                        returnList.append(matrix[i][j])
                        j -= 1
                elif t == 3:
                    j += 1
                    i -= 1
                    if i <= r:
                        break
                    while i > r:
                        returnList.append(matrix[i][j])
                        i -= 1

        return returnList