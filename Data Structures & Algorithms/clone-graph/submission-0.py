"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        elif len(node.neighbors) == 0:
            return Node(node.val)
        else:
            visited = set()
            refs = {}
            toVisit = deque()
            toVisit.append(node)


            while toVisit:
                ptr = toVisit.popleft()

                if ptr.val in visited:
                    continue
                visited.add(ptr.val)
                if ptr.val not in refs.keys():
                    refs[ptr.val] = Node(ptr.val)

                for neighbor in ptr.neighbors:
                    try:
                        refs[ptr.val].neighbors.append(refs[neighbor.val])
                    except:
                        refs[neighbor.val] = Node(neighbor.val)
                        refs[ptr.val].neighbors.append(refs[neighbor.val])
                    toVisit.append(neighbor)
        return refs[1]