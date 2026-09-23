# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rtv = deque([root])
        def isSubRoot(node1, node2):
            if node1 == None and node2 == None:
                return True
            if node1 == None or node2 == None:
                return False
            # print(f"root : {node1.val}, subroot : {node2.val}")
            if node1.val == node2.val:
                if isSubRoot(node1.left, node2.left) and isSubRoot(node1.right, node2.right):
                    return True
            return False
        while rtv:
            node = rtv.popleft()
            if isSubRoot(node, subRoot):
                return True
            else:
                if node.left != None:
                    rtv.append(node.left)
                if node.right != None:
                    rtv.append(node.right)
        return False