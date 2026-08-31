class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Solve Using Kahn's Algorithm
        # 1. Build graph.
        # 2. Calculate indegree.
        # 3. Put all indegree-0 courses into queue.
        # 4. Process them.
        # 5. Reduce indegree of dependent courses.
        # 6. Count how many courses were processed.
        # 7. If processed count equals `numCourses`, return `True`.

        # 1. build graph
        graph = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)

        # calculate indegree:
        indegree = [0] * numCourses
        for node in graph:
            for nei in graph[node]:
                indegree[nei] += 1

        # Add thode node into q which has indegree 0:
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        res = 0
        # start doing bfs 
        while q:
            # process node 
            node = q.popleft()
            res += 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if res == numCourses:
            return True
        else:
            return False


        