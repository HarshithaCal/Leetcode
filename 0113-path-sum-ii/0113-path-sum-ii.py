# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, currpath):
            if node is None:
                return 

            currpath.append(node.val)

            # Checking if it is a leaf node and the path sum matches targetSum
            if node.left is None and node.right is None and sum(currpath) == targetSum:
                # Use currpath[:] so we append a copy, not the original list
                res.append(currpath[:])

            dfs(node.left, currpath)
            dfs(node.right, currpath)

            currpath.pop()
            return res

        if root:
            return dfs(root, [])
        else:
            return []