# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        pIndex = 0
        def seacrch(left, right, val):
            for i in range(left, right+1):
                if inorder[i] == val:
                    return i

        # node creation
        def dfs(left, right):

            nonlocal pIndex
            if left > right:
                return None
            root_val = preorder[pIndex]
            root = TreeNode(root_val)
            iIndex = seacrch(left, right, root_val)
            pIndex += 1
            root.left = dfs(left, iIndex - 1)
            root.right = dfs(iIndex+1, right)
            return root
        
        return dfs( 0, len(inorder)-1)

