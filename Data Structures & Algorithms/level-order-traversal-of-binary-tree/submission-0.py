# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ntv = deque([[root, 0]])
        solution = []
        while ntv:
            node, lvl = ntv.popleft()
            try:
                solution[lvl].append(node.val)
            except:
                solution.append([node.val])
            
            if node.left is not None:
                ntv.append([node.left, lvl + 1])
            if node.right is not None:
                ntv.append([node.right, lvl + 1])
        return solution