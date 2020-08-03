class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters
        p = 0
        res = 0
        for i in range(len(houses)):
            h = houses[i]
            while p+1 < len(heaters)-1 and heaters[p+1] < h:
                p += 1
            res = max(res, min(abs(h-heaters[p]), abs(heaters[p+1] - h)))
        return res