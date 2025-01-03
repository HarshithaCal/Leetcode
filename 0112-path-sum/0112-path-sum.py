# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False

            print("node value is ", node.val)

            currSum += node.val
            print("curr sum is ", currSum)

            if not node.left and not node.right and currSum == targetSum:
                return True 
            
            return dfs(node.left, currSum) or dfs(node.right, currSum)
        
        if root:
            return dfs(root, 0)
        else:
            return False

        