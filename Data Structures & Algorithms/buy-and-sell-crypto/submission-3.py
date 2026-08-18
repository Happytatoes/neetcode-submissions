class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # edge case: if only one long

        result = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            #print(prices[sell])
            #print(prices[buy])
            profit = prices[sell] - prices[buy]
            result = max(profit, result)

            # if we are not profitable, move both pointers forward
            if profit < 0 and buy + 1 != len(prices):
                buy += 1
                sell = buy + 1
            # otherwise, move just the sell date forward
            else:
                sell += 1
        
        return result




                
            
            