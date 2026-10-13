class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfsVisit(i,j):
            nonlocal grid
            if i >= len(grid) or i < 0:
                return
            if j >= len(grid[i]) or j < 0:
                return
            if grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfsVisit(i+1,j)
            dfsVisit(i,j+1)
            dfsVisit(i-1,j)
            dfsVisit(i,j-1)
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    # for line in grid:
                    #     print(line)
                    # print()
                    dfsVisit(i,j)
                    counter += 1

        return counter