# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None:
            return []

        queue = deque([root]) # 1 | 
        while queue and len(queue) > 0:
            length = len(queue) # length = 1
            curr_lvl = []
            for i in range(length-1, -1, -1): # i = 
                root = queue.popleft() # root = 
                curr_lvl.append(root.val)
                if root.left != None:
                    queue.append(root.left)
                if root.right != None:
                    queue.append(root.right) #
            res.append(curr_lvl)
        return res
            




        