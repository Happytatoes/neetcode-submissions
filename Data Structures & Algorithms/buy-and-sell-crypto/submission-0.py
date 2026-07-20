class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        max_profit = 0
        n = len(prices)

        for i in range(0, n):
            buy = prices[i]
            later_array = []

            for j in range(i, n):
                later_array.append(prices[j])

            sell = max(later_array)
            profit = sell - buy
            if profit > max_profit:
                max_profit = profit

        return max_profit