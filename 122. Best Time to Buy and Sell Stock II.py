from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                max_profit += diff
        return max_profit


# input = [7,1,5,3,6,4]
input = [1,2,3,4,5]
# input = [7,6,4,3,1]
output = Solution().maxProfit(input)
print(output)

