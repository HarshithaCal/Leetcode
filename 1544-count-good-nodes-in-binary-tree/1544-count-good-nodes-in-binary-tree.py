# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxi):
            if not node:
                return 0

            if node.val >= maxi:
                total = 1  
            else:
                total =  0
            
            new_maxi = max(maxi, node.val)

            total += dfs(node.left, new_maxi)
            total += dfs(node.right, new_maxi)
            
            return total

        if not root:
            return 0
        return dfs(root, root.val)