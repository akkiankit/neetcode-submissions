class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                current_profit = prices[j] - prices[i]
                if max_profit < current_profit:
                    max_profit = current_profit
        return max_profit
