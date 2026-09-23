# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ntv = deque([root])
        while ntv:
            node = ntv.popleft()

            if node.val > max(p.val, q.val):
                ntv.append(node.left)
            elif node.val < min(p.val, q.val):
                ntv.append(node.right)
            else:
                return node
        return None