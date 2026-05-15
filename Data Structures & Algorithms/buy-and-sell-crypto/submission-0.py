class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lower = prices[0]
        profit = 0

        for i in prices:

            if i < lower:
                lower = i
            if i > lower and i - lower > profit:

                profit = i - lower

        return profit

            