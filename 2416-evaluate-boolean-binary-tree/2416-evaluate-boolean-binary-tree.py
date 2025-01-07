# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # 2- OR, 3- AND, 0 - False, 1 - True
        if root is None:
            return root.val

        def dfs(node):

            if node.left is None and node.right is None:
                return node.val != 0
            
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            
            if node.val == 2: #OR
                node.val = left_node or  right_node
            else:
                # print(left_node.val, right_node.val)
                node.val = left_node and right_node
            
            return node.val
        
        return dfs(root)

        