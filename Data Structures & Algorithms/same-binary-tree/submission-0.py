# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameHelper(self, p, q) -> bool:
        if p == None and q == None:
            return True
        try:
            if p.val == q.val:
                if self.isSameHelper(p.left, q.left) and self.isSameHelper(p.right, q.right):
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSameHelper(p,q)