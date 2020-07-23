# 二分法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 2:
            return True
        left = 1
        right = num//2
        while left <= right:
            mid = left + (right - left) //2
            mid_2 = mid ** 2
            if mid_2 == num:
                return True
            elif mid_2 < num:
                left = mid + 1
            else :
                right = mid - 1
        return False

# 牛顿迭代
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <=2:
            return True
        x = num //2
        while x ** 2 - num > 0:
            x = (x + num//x) // 2
        return x **2 == num

# num = 2000105819
num = 2
print(Solution().isPerfectSquare(num))