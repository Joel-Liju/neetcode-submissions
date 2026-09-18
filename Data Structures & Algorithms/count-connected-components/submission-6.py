class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n)]

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return x
        
        def union(x,y):
            parent[find(y)] = find(x)

        for edge in edges:
            union(edge[0], edge[1])
        # print(parent)
        return sum([1 if i == x else 0 for i, x in enumerate(parent)])