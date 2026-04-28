class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         diff = prices[j] - prices[i]
        #         if diff > profit:
        #             profit = diff
        # return profit
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if min_price > price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit

            

                