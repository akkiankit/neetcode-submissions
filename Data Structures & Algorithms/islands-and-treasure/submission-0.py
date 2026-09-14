class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #since the problem is distance to it nearest treasour meand min_dis so BFS guarantees shortest distance in an unweighted graph and since there will be multiple treasure chest it is multi source bfs
        # row and cols of grid
        ROWS = len(grid)
        COLS = len(grid[0])
        # store the 
        q = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row,col))
        
        # now we need to find the nearest land in all direction so direction check
        directions = [(-1,0), (1, 0), (0, -1), (0,1)]

        # now let's apply bfs to find min distance
        while q:

            row, col = q.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 2147483647:
                    continue

                grid[nr][nc] = grid[row][col] + 1
                q.append((nr, nc))

        