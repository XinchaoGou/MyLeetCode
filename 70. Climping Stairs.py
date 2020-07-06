class Solution:

    # 动态规划，用数组存储
    # def climbStairs(self, n: int) -> int:
    #     if (n == 1):
    #         return 1
    #     elif(n ==2):
    #         return 2
    #     n_list = [0] *  (n+1)
    #     n_list[1] = 1
    #     n_list[2] = 2
    #     for i in range(3, n+1):
    #         n_list[i] = n_list[i-1] +n_list[i-2]
    #     return n_list[n]

    # 动态规划， 不用数组存储
    def climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1
        elif(n ==2):
            return 2
        climb_1 = 2
        climb_2 = 1
        for i in range(3, n+1):
            cur = climb_1 +climb_2
            climb_2 = climb_1
            climb_1 = cur
        return cur


input = 38

output = Solution().climbStairs(input)
print(output)
