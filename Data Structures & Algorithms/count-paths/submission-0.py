class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = []
        for i in range(m):
            tmpArry = []
            for j in range(n):
                tmpArry.append(0)
            paths.append(tmpArry)
        
        for i in range(m):
            paths[i][0] = 1
        for j in range(n):
            paths[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[-1][-1]