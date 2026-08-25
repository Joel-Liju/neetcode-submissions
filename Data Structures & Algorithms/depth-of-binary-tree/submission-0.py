# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        arr = [[root, 1]]
        maxLength = 1
        while len(arr) != 0:
            tempVal = arr.pop()
            maxLength = max(maxLength, tempVal[1])
            try:
                if tempVal[0].left != None:
                    arr.append([tempVal[0].left, tempVal[1] + 1])
            except:
                pass
            try:
                if tempVal[0].right != None:
                    arr.append([tempVal[0].right, tempVal[1] + 1])
            except:
                pass
        return maxLength