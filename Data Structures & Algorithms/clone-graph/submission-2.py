"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # bfs appraoch
        if not node:
            return None
        old_to_new = {}
        copy = Node(node.val)
        old_to_new[node] = copy
        q = deque([node])
        while q:
            c_node = q.popleft()
            for nei in c_node.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    q.append(nei)
                old_to_new[c_node].neighbors.append(old_to_new[nei])
        return old_to_new[node]        

        # # dfs approach
        # if node is None:
        #     return None
        # old_to_new = {}
        # def dfs(node):
        #     # if node in already cloned then return just node
        #     if node in old_to_new:
        #         return old_to_new[node]
        #     # deep copy of current node
        #     copy = Node(node.val)
        #     # add the copied node to dictionary
        #     old_to_new[node] = copy

        #     # check neighbours of current node
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))
        #     return copy

        # return dfs(node)

        