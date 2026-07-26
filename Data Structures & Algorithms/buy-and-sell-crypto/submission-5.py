class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('infinity')
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(prices[i] - min_price, max_profit)
        return max_profit
        # l, r = 0, 1
        # res = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         res = max(res, profit)
        #     else:
        #         l = r
        #     r += 1
        # return res
        
        # res = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         res = max(res, sell - buy)
        # return res
        