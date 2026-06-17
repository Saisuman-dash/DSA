class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p=0
        n = len(prices)
        max_profit = 0
        min_price = float('inf')
        for i in range(0,n):
            min_price = min(min_price,prices[i])
            max_profit = max(prices[i]-min_price,max_profit)
        return max_profit
               
      
    
        