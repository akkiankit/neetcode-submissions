class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Define a graph first
        graph = {i:[] for i in range(numCourses)}

        # 2. Build graph from prerequise
        for u, v in prerequisites:
            graph[u].append(v)

        # 3. find the indegree of course
        indeg = [0] * numCourses
        for node in graph:
            for neig in graph[node]:
                indeg[neig] += 1

        # 4. Assign those node to q which has indegree of 0
        q = deque()
        for c in range(numCourses):
            if indeg[c] == 0:
                q.append(c)

        # 5. now apply bfs to find the 
        res = []
        cnt = 0
        while q:
            # first node
            node = q.popleft()
            cnt += 1
            res.append(node)

            # now reduce the indegree for node neighbour
            for nei in graph[node]:
                indeg[nei] -= 1

                # check whether the nei has indegree of 0 if yes then add it to q
                if indeg[nei] == 0:
                    q.append(nei)
        
        if cnt != numCourses:
            return []
        return res[::-1]

        

        