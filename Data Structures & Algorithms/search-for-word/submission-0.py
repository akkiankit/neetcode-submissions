class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])


        def dfs(row, col, i):
            # base condition - condition met
            if i == len(word):
                return True
            # non ideal condition 
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] != word[i]:
                return False

            # Mark current cell visited
            temp = board[row][col]
            board[row][col] = "#"
            
            # if condition met then we need to search in all direction
            found = dfs(row, col+1, i+1) or dfs(row, col-1, i + 1) or dfs(row+1, col, i+1) or dfs(row-1, col, i+1)

            # return temp 
            board[row][col] = temp

            return found

        # try every cell as a starting point
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return False
        