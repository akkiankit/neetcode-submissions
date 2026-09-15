class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # bfs approach
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([(0, -1)])
        visted = set()
        visted.add(0)
        while q:
            node, parent = q.popleft()
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visted:
                    return False
                
                visted.add(nei)
                q.append((nei, node))

        return len(visted) == n
        

        # # Approach 2 — Explicit Cycle Detection
        # graph = {i:[] for i in range(n)}
        # for u,v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # # cyclic detection
        # visited= set()
        # def dfs(node, parent):
        #     visited.add(node)
        #     for nei in graph[node]:
        #         if nei == parent:
        #             continue
        #         if nei in visited:
        #             return False
        #         if not dfs(nei, node):
        #             return False
        #     return True
        # if not dfs(0, -1):return False

        # return len(visited) == n

        # # dfs approach.
        # # for a graph to be valid it edges should be less than the number of node 
        # # Tree must have n - 1 edges.
        # # 1. Every node is connected
        # # 2. There is no cycle
        # # If it does:
        # #     check whether every node is connected.
        # if len(edges) != n -1:
        #     return False

        # # initial 
        # graph = {i:[] for i in range(n)}
        # # build the graph
        # for u,v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        # # now checking if each node is connected or not
        # visited = set()
        # def dfs(node):
        #     visited.add(node)
        #     for nei in graph[node]:
        #         if nei not in visited:
        #             dfs(nei)
        # dfs(0)
        # return len(visited) == n
        


        