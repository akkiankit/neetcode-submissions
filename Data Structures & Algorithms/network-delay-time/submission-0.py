class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1 Build the weighted graph
        graph = {i:[] for i in range(1, n+1)}
        for u, v, t in times:
            graph[u].append((v,t))

        #2. initialize the distance and first distance should be 0
        dis = [float('inf')] * (n+1)
        dis[k] = 0
        # Initialize the heap with dis and sorce node
        heap = [(0, k)]

        # while loop to iterate through each node of a graph
        while heap:
            # pop the initial node with current dis
            curr_dis, node = heapq.heappop(heap)

            # if curr_dis is more than the previous then just bypass it
            if curr_dis > dis[node]:
                continue

            # iterate thourgh each neig
            for v, t in graph[node]:
                new_dis = curr_dis + t
                if new_dis < dis[v]:
                    dis[v] = new_dis
                    heapq.heappush(heap,(new_dis, v))

        answer = max(dis[1:])

        if answer == float("inf"):
            return -1

        return answer



        