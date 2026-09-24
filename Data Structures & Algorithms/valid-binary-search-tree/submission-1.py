# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidSubBST(node, ll, ul):
            if node == None:
                return True
            if ll < node.val and node.val < ul:
                return isValidSubBST(node.left, ll, node.val) and isValidSubBST(node.right, node.val, ul)
            else:
                return False
        lowerLimit = float('-inf')
        upperLimit = float('inf')

        if root == None:
            return True

        return isValidSubBST(root, lowerLimit, upperLimit)