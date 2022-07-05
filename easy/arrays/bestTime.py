# best time to buy and sell stock II
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/

from os import O_ACCMODE


class Solution():
    # adding every increasing difference (immediate pos dist)
    def maxProfit(self, prices: list) -> int:
        if not prices: return 0

        profit = 0
        for i in range(0, len(prices) - 1):
            dif = prices[i + 1] - prices[i] 
            if dif > 0:
                profit += dif
            
        return profit

    # just adding increasing sequences, but we're not adding until we get the whole increasing sequence (max pos dist)
    def maxProfit2(self, prices: list) -> int:
        profit = 0
        low = prices[0] if prices else 0

        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                continue
            else:
                dif = prices[i-1] - low
                if dif > 0: profit += dif
                low = prices[i]
        
        # this will capture any continuously increasing sequences
        profit += prices[-1] - low
        return profit 

s = Solution()
print(s.maxProfit([7,1]))
    
