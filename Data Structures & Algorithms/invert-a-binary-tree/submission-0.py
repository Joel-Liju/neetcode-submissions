# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertHelper(self, ptr):
        if ptr != None:
            self.invertHelper(ptr.left)
            self.invertHelper(ptr.right)

            temp = ptr.left
            ptr.left = ptr.right
            ptr.right = temp

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertHelper(root)

        return root