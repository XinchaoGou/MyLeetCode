from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        max_pro = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            p = prices[i]
            profit = p - lowest
            if profit > max_pro:
                max_pro = profit
            if p < lowest:
                lowest = p
        return max_pro

input = [7,1,5,3,6,4]
output = Solution().maxProfit(input)
print(output)