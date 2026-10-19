class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMatrix = { i:[] for i in range(n)}
        for edge in edges:
            adjMatrix[edge[0]].append(edge[1])
            adjMatrix[edge[1]].append(edge[0])
        def dfs(prev, node, visited):
            # print(prev, node, visited, adjMatrix[node])
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adjMatrix[node]:
                if neighbor != prev:
                    if not dfs(node, neighbor, visited):
                        return False
            return True
        visited = set()
        flag = dfs(-1, 0, visited)
        return flag and len(visited) == n