# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def checkSym(p, q):
            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False
            
            if p.val != q.val:
                return False
            
            
            return checkSym(p.left, q.right) and checkSym(p.right, q.left)
        
        return checkSym(root.left, root.right)