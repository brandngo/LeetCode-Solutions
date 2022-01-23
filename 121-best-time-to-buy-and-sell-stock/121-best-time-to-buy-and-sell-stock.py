class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = 0
        profit = 0
        for i in range(len(prices)):
          if i == 0:
            low = prices[i]
            high = prices[i]
          else:
            if low > prices[i]:
              low = prices[i]
              high = prices[i]
            elif prices[i] > high:
              high = prices[i]
              profit = max(profit, high-low)
        
        return profit
              