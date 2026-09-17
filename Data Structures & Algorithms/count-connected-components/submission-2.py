class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        counter = 0

        edgesDict = {}

        for edge in edges:
            try:
                edgesDict[edge[0]].add(edge[1])
            except:
                edgesDict[edge[0]] = set()
                edgesDict[edge[0]].add(edge[1])
            try:
                edgesDict[edge[1]].add(edge[0])
            except:
                edgesDict[edge[1]] = set()
                edgesDict[edge[1]].add(edge[0])
        def dfs(i):
            nonlocal visited, edgesDict
            if visited[i]:
                return
            visited[i] = True
            try:
                for edge in edgesDict[i]:
                    dfs(edge)
            except:
                return

        for i in range(n):
            # print(visited)
            if not visited[i]:
                counter += 1
                dfs(i)

        return counter
