#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#

import collections
# @lc code=start
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        ht = collections.defaultdict(list)
        for i in range(len(ring)):
            ht[ring[i]].append(i)
        
        dp = [0] * len(ring)
        pre_list = [0]
        for i in range(len(key)):
            c = key[i]
            ht_list = ht[c]
            last = float('inf')
            for j in range(len(ht_list)):
                idx = ht_list[j]
                min_v = float('inf')
                for k in pre_list:
                    diff = abs(k- idx)
                    min_v = min(min_v, min(diff, len(ring) - diff) + dp[k])
                dp[idx] = min_v
                last = min(last, min_v)
            pre_list = ht_list
        return last + len(key)
                

# @lc code=end
# ring = "godding"
# key = "gd"

ring = "godding"
key = "godding"
print(Solution().findRotateSteps(ring, key))

 
