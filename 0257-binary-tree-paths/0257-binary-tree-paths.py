# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def dfs(root, path = ""):

            if root is None:
                return None

            if root.left is None and root.right is None: #leaf node
                paths.append(path+str(root.val))
                return paths

            dfs(root.left, path+str(root.val)+"->")
            
            dfs(root.right, path+str(root.val)+"->")
        
            return paths

            
        if root:
            return dfs(root, "")
        else:
            return None
        