class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         current_profit = prices[j] - prices[i]
        #         if max_profit < current_profit:
        #             max_profit = current_profit
        # return max_profit
        min_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            profit = 0
            if min_price > prices[i]:
                min_price = prices[i]
               
            else:
                profit = prices[i] - min_price

                if max_profit < profit:
                    max_profit = profit
        return max_profit


