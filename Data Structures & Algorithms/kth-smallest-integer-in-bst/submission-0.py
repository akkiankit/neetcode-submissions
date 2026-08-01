# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root: Optional[TreeNode], li = List[int]):
        if root == None:
            return 0
         
        left = self.inorder(root.left, li)
        li.append(root.val)
        right = self.inorder(root.right, li)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_lis = []
        self.inorder(root, sorted_lis)
        # print(sorted_lis)
        return sorted_lis[k-1]

        
        # soeted_num = []
        # if root == None:
        #     return 0

        # left = self.kthSmallest(root.left)
        # print(root.val)
        # right = self.kth

        
        