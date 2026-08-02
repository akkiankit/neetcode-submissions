# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not(left < node.val < right):
                return False
            
            left_con = valid(node.left, left, node.val)
            right_con = valid(node.right, node.val, right)

            return left_con and right_con

        return valid(root, float("-inf"), float("inf"))
        
        


        