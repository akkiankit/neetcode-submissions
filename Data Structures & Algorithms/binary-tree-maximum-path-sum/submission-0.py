# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0

            leftmax = dfs(node.left)
            rightmax = dfs(node.right)

            leftmax = max(0, leftmax)
            rightmax = max(0, rightmax)

            current_sum = node.val + leftmax + rightmax
            max_sum = max(max_sum, current_sum)

            return node.val + max(leftmax, rightmax)
        dfs(root)
        return max_sum


        