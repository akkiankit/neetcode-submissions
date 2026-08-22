class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1

            if row >= m or col >= n:
                return 0

            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = (
                dfs(row, col + 1) +
                dfs(row + 1, col)
            )

            return memo[(row, col)]

        return dfs(0, 0)

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:

#         def dfs(m, n, row, col):
#             # base case
#             if row == m - 1 and col == n - 1:
#                 return 1

#             if row >= m or col >= n or row < 0 or col < 0:
#                 return 0

    
#             res = dfs(m, n, row, col + 1) + dfs(m, n, row+1, col)
#             return res
        
#         return dfs(m, n, 0,0)
        

        