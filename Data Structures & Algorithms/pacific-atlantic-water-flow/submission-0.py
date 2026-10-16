class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pSet = set()
        aSet = set()
        visited = set()
        for j in range(len(heights[0])):
            pSet.add((0,j))
            aSet.add((len(heights)-1, j))
        for i in range(len(heights)):
            pSet.add((i,0))
            aSet.add((i, len(heights[0])-1))
        
        def hitsOcean(loc, visited, oSet) -> bool:
            # print("func : ", loc)
            # print("Temp : ", oSet)
            if loc in oSet:
                return True
            if loc in visited:
                return False
            if 0 <= loc[0] < len(heights) and 0 <= loc[1] < len(heights[0]):
                visited.add(loc)
                if loc[1] + 1 < len(heights[0]) and heights[loc[0]][loc[1]] >= heights[loc[0]][loc[1] + 1] and hitsOcean((loc[0], loc[1] + 1), visited, oSet):
                    oSet.add(loc)
                    return True

                if loc[1] - 1 >= 0 and  heights[loc[0]][loc[1]] >= heights[loc[0]][loc[1] - 1] and hitsOcean((loc[0], loc[1] - 1), visited, oSet):
                    oSet.add(loc)
                    return True

                if loc[0] + 1 < len(heights) and  heights[loc[0]][loc[1]] >= heights[loc[0] + 1][loc[1]] and hitsOcean((loc[0] + 1, loc[1]), visited, oSet):
                    oSet.add(loc)
                    return True

                if loc[0] - 1 >= 0 and heights[loc[0]][loc[1]] >= heights[loc[0]  - 1][loc[1]] and hitsOcean((loc[0] - 1, loc[1]), visited, oSet):
                    oSet.add(loc)
                    return True
                return False
            else:
                return False
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                # print("og : ", (i,j))
                # print("set : ", pSet)
                hitsOcean((i,j), set(), pSet)
                # print()
                hitsOcean((i,j), set(), aSet)
        # print(sorted(list(pSet)))
        # print(sorted(list(aSet)))
        return list(pSet.intersection(aSet))