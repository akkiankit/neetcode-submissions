class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # finding the rows and cols
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        def dfs(row,col):
            if row <0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row,col))
            area = 1

            area += dfs(row-1, col) # up
            area += dfs(row+1, col) # down
            area += dfs(row, col - 1) # left
            area += dfs(row, col + 1)
            return area
        
        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == 1:
                    current_area = dfs(row, col)
                    max_area = max(current_area, max_area)

        return max_area


        