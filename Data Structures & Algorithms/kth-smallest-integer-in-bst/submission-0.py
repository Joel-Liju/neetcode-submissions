# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sol = -1

        def dfs(node, num):
            nonlocal k, sol
            if not node:
                return num
            if node.left:
                num = dfs(node.left, num)
            num += 1
            # print(num, node.val, k)
            if num == k:
                sol = node.val
                # print(sol)
            if node.right:
                num = dfs(node.right, num)
            return num
        dfs(root, 0)
        return sol