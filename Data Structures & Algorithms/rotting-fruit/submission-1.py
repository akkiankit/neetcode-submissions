class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Grid + Multi-Source BFS + Levels
        # find row and cols
        ROWS = len(grid)
        COLS = len(grid[0])
        # create initial queue and fresh count
        q = deque()
        fresh = 0
        # cound the rotten fruit because that will be the source because bananane will start getting rotten
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1
        # now we have fresh and initial source let's count the minutes that must elapse untill there are zero frsh fruits
        # fruit can get rotten in all direction so let's create direction
        direction = [
            (-1, 0), # up
            (1, 0), # down
            (0, -1), # left
            (0, 1) # right
        ]
        
        minutes = 0
        # now start checking the fresh fruits from source
        while q and fresh > 0: # run the while loop untill fresh fruit is more than 0
            # since we are going level by level checking so let's fetch the current level length
            level_len = len(q)
            for _ in range(level_len):
                row, col = q.popleft() # we have current rotten fruit and let's check in all direction if fresh fruit is there around then it will get rotten. so check in all direction
                for nr, nc in direction:
                    r = row + nr
                    c = col + nc
                    # checking the condition of r and c in all direction and if it is other then fresh then continue
                    if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c]!=1):
                        continue
                    grid[r][c] = 2
                    # now reduce the count
                    fresh -= 1
                    # add this current rotten in q
                    q.append((r,c))
            minutes += 1
        if fresh == 0:
            return minutes
        return -1


         