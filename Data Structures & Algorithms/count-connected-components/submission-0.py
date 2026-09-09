class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        components = 0
        for node in graph:
            if node not in visited:
                dfs(node)
                components += 1
        return components
        