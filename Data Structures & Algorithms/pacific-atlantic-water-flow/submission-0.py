class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        # this is again the multi source prblem where water can flow from atlantic to pacific and vice versa
        pacific = set()
        atlantic = set()

        # to check the water flow
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # 
        def dfs(row, col , visited):
            visited.add((row,col))

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited or heights[nr][nc] < heights[row][col]:
                    continue
                dfs(nr, nc, visited)
        for col in range(COLS):
            dfs(0, col, pacific)
            dfs(ROWS - 1, col, atlantic)

        for row in range(ROWS):
            dfs(row, 0, pacific)
            dfs(row, COLS - 1, atlantic)

        result = []

        for row in range(ROWS):
            for col in range(COLS):
                if (
                    (row, col) in pacific and
                    (row, col) in atlantic
                ):
                    result.append([row, col])

        return result
        