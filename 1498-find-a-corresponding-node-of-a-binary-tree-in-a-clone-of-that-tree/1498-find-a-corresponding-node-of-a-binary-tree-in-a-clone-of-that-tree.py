# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ### Iterative: BFS. BFS means queue
        # BFS - root, left, right
        # Initialize queues for BFS traversal
        queue_original = deque([original])
        queue_cloned = deque([cloned])
        
        while queue_original:
            # Get the current nodes from both trees
            current_original = queue_original.popleft()
            current_cloned = queue_cloned.popleft()
            
    
            if current_original == target:
                return current_cloned 
            
            # Add left children to the queue
            if current_original.left:
                queue_original.append(current_original.left)
                queue_cloned.append(current_cloned.left)
            
            # Add right children to the queue
            if current_original.right:
                queue_original.append(current_original.right)
                queue_cloned.append(current_cloned.right)
        
        return None  # If target is not found (unlikely based on problem description)






        # #########pre-order + DFS. DFS means stack
        # if original is None:
        #     return None

        # # if original == cloned == target:  -- #original and cloned are different tree nodes so this is not satisfied
        # if original == target:
        #     return cloned
                
        # left_result = self.getTargetCopy(original.left, cloned.left, target)
        # if left_result is not None:
        #     return left_result

        # return self.getTargetCopy(original.right, cloned.right, target)

        # ################## inorder - DFS
        # def inorder(o: TreeNode, c: TreeNode):
        #     if o:
        #         inorder(o.left, c.left)
        #         if o is target:
        #             self.ans = c

        #         inorder(o.right, c.right)
                
        # inorder(original, cloned)
        # return self.ans 
    
        


        