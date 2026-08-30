class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0" or (row, col) in visited:
                return 

            visited.add((row, col))

            dfs(row-1, col) # up
            dfs(row+1, col) # down
            dfs(row, col-1) # left
            dfs(row, col + 1) # rihgt

            return True

        islandcount = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == "1":
                    if dfs(row, col):
                        islandcount += 1
        return islandcount



        