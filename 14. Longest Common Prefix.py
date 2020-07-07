class Solution:
    # def longestCommonPrefix(self, strs) -> str:
    #     result = ''
    #     if len(strs) == 0:
    #         return result
    #     for i in range(len(strs[0])):
    #         temp_str = strs[0][i]
    #         for j in range(1, len(strs)):
    #             if i>=len(strs[j]) or temp_str != strs[j][i]:
    #                 return result
    #         result += temp_str
    #     return result
    def longestCommonPrefix(self, strs) -> str:
        results = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                results += i[0]
            else:
                break
        return results

input = ["aa","a"]
print(Solution().longestCommonPrefix(input))