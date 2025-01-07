# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        #pre-order

        # print(f"original: {original} and cloned: {cloned}")
        
        if original is None:
            return None

        # if original == cloned == target:  -- #original and cloned are different tree nodes so this is not satisfied
        if original == target:
            return cloned
        
        
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result is not None:
            return left_result

        return self.getTargetCopy(original.right, cloned.right, target)
    
        


        