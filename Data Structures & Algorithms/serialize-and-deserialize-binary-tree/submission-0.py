# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Convert a tree into a list/string, then rebuild the same tree from it.

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []
        def dfs(root):
            if not root:
                values.append('None')
                return

            values.append(str(root.val))
            left = dfs(root.left)
            right = dfs(root.right)
           
        dfs(root)
        return ",".join(values)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(","))

        def dfs():
            value = next(values)
            if value == "None":
                return None
            root = TreeNode(int(value))
            root.left = dfs()
            root.right = dfs()
            
            return root

        return dfs()
        

        



