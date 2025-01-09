# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return
        print(val, root.val)
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val == root.val:
            print("equal", root)
            return root
        else:
            return self.searchBST(root.right, val)

        