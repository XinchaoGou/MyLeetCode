#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#
import collections
from typing import List
import heapq
from collections import deque
# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # 用cnt个num去匹配前面的begin节点
        def match_tail(num, cnt):
            nonlocal b_stack
            for i in range(cnt):
                if num - b_stack.popleft()<2:
                    return False
            return True
        
        # 增加新的 begin节点
        def add_begin(num, cnt):
            nonlocal b_stack
            for j in range(cnt):
                b_stack.append(num)

        if len(nums)< 3:
            return False
        # 统计每个数字的次数stat是一个list,[[num1, cnt1], [num2, cnt2],...] 
        stat = [[nums[0], 1]]
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                stat[-1][1] += 1
            else:
                stat.append([nums[i+1], 1])
        
        # 先把第一个节点添加进 栈
        b_stack = deque()
        add_begin(nums[0], stat[0][1])

        for i in range(len(stat)-1):
            cur = stat[i+1]
            pre = stat[i]
            # 当前num2的比前一个num1大一, 说明是连续的序列
            if cur[0] - pre[0] == 1:
                cnt = cur[1] - pre[1]
                # 次数增加, 增加新的节点
                if cnt > 0:
                    add_begin(cur[0], cnt)
                # 次数减少, 说明pre是某一个序列的末尾节点
                elif cnt < 0:
                    if not match_tail(pre[0], -cnt): return False
            # 数字差超过一, 说明是新的序列
            else:
                # 先把所有末尾节点匹配完
                if not match_tail(pre[0], pre[1]): return False
                # 再把新的头节点添加进去
                for j in range(cur[1]):
                    b_stack.append(cur[0])
        if not match_tail(cur[0], cur[1]): return False
        if b_stack:
            return False
        return True


        
# @lc code=end



# 哈希表 + 最小堆
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            if mp.get(x-1):
                length = heapq.heappop(mp[x-1])
                heapq.heappush(mp[x], length + 1)
            else:
                heapq.heappush(mp[x], 1)
        return not any(q and q[0] < 3 for q in mp.values())

# 贪心 + 2个哈希表
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = collections.Counter(nums)
        endMap = collections.Counter()

        for x in nums:
            if (count := countMap[x]) > 0:
                if (prevEndCount := endMap.get(x - 1, 0)) > 0:
                    countMap[x] -= 1
                    endMap[x - 1] = prevEndCount - 1
                    endMap[x] += 1
                else:
                    if (count1 := countMap.get(x + 1, 0)) > 0 and (count2 := countMap.get(x + 2, 0)) > 0:
                        countMap[x] -= 1
                        countMap[x + 1] -= 1
                        countMap[x + 2] -= 1
                        endMap[x + 2] += 1
                    else:
                        return False
        return True

# nums = [1,2,3,5,6,7]
# nums = [1,2,3,3,4,4,5,5]
nums = [1,2,3,4,4,5]
print(Solution().isPossible(nums))