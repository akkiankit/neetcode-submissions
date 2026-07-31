# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # DFS Approach
        # if root is None:
        #     return None

        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # root.left, root.right = right, left
        # return root

        # BFS approach
        if not root: return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # print(node.val)

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

        