
class Solution:

    # def permute(self, nums):
    #     if len(nums) == 1:
    #         return [[nums[0]]]
    #
    #     result = []
    #     for i in range(len(nums)):
    #         num_i = nums[i]
    #         res_list = nums[:]
    #         res_list.pop(i)
    #         res_permute = self.permute(res_list)
    #         for j in range(len(res_permute)):
    #             res_permute[j].insert(0, num_i)
    #             result.append(res_permute[j])
    #
    #     return result


    def permute(self, nums):
        import copy
        if not nums:
            return
        if len(nums) == 1:
            return nums

        def dfs(res, nums, path):
            if len(nums) == 0:
                res.append(path)

            for i, v in enumerate(nums):
                s_path = path[:]
                s_path.append(v)
                dfs(res, nums[:i] + nums[i + 1:], s_path)

        res = []
        dfs(res, nums, [])
        return res

    # def permute(self, nums):
    #     res = []
    #
    #     def dfs(res, nums, path):
    #         if len(nums) <= 1:
    #             res.append(path + nums)
    #             return
    #         for i, v in enumerate(nums):
    #             dfs(res, nums[:i] + nums[i + 1:], path + [v])
    #
    #     dfs(res, nums, [])
    #     return res

my_input = [1, 2, 3]
output = Solution().permute(my_input)
print(output)
