class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMatrix = {i:[] for i in range(numCourses)}

        for prereq in prerequisites:
            try:
                adjMatrix[prereq[0]].append(prereq[1])
            except:
                adjMatrix[prereq[0]] = [prereq[1]]
        
        def dfs(visited, course):
            nonlocal adjMatrix
            if course in visited:
                return False
            if len(adjMatrix[course]) == 0:
                return True
            visited.add(course)
            for prereq in adjMatrix[course]:
                if not dfs(visited, prereq):
                    return False
                else:
                    adjMatrix[course].remove(prereq)
            return True
        for key in adjMatrix.keys():
            visited = set()
            if not dfs(visited, key):
                return False
        return True