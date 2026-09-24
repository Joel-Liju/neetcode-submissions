# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidSubBST(node, ll, ul):
            if not node:
                return True
            if not(ll < node.val < ul): return False

            return isValidSubBST(node.left, ll, node.val) and isValidSubBST(node.right, node.val, ul)

        return isValidSubBST(root, float('-inf'), float('inf'))