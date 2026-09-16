class Solution:
    def climbStairs(self, n: int) -> int:
        # 3. top down
        if n <=2:
            return n
        dp = [0] * (n+1) # creating the state
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]
        # memo = {}
        # def dfs(n):
        #     if n == 1:
        #         return 1

        #     if n == 2:
        #         return 2

        #     if n in memo:
        #         return memo[n]

            
        #     memo[n] = dfs(n-1) + dfs(n-2)

        #     return memo[n]
        # return dfs(n)

        # if n == 1:
        #     return 1

        # if n == 2:
        #     return 2

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        