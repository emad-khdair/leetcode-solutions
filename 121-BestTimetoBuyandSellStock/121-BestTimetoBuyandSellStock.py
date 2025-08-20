# Last updated: 8/19/2025, 5:15:31 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0 , 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                if profit > max_profit:
                    max_profit = profit
                sell += 1
            else:
                buy = sell
                sell += 1

        return max_profit