class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs approach.
        # for a graph to be valid it edges should be less than the number of node 
        # Tree must have n - 1 edges.
        # 1. Every node is connected
        # 2. There is no cycle
        # If it does:
        #     check whether every node is connected.
        if len(edges) != n -1:
            return False

        # initial 
        graph = {i:[] for i in range(n)}
        # build the graph
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # now checking if each node is connected or not
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        dfs(0)
        return len(visited) == n
        


        