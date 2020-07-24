def permutation(t_list, k):
    res = []
    if k == 1:
        for i in range(len(t_list)):
            res.append([t_list[i]])
        return res
    for i in range(len(t_list)):
        v = t_list.pop(i)
        permutation_list = list(map(lambda x: [v] + x, permutation(t_list, k - 1)))
        res.extend(permutation_list)
        t_list.insert(i, v)
    return res

def combination(t_list, k):
    res = []
    if k == 1:
        for i in range(len(t_list)):
            res.append([t_list[i]])
    for i in range(len(t_list)):
        v = t_list[i]
        combination_list = list(map(lambda x: [v] + x, combination(t_list[i+1:], k-1)))
        res.extend(combination_list)
    return res

# print(combination([1,2,3,4],0))

from typing import List
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def combination(t_list, k):
            res = []
            if k == 1:
                for i in range(len(t_list)):
                    res.append([t_list[i]])
            for i in range(len(t_list)):
                v = t_list[i]
                combination_list = list(map(lambda x: [v] + x, combination(t_list[i + 1:], k - 1)))
                res.extend(combination_list)
            return res

        def all_time(n, p="h"):
            if p == "h":
                t_list = [8, 4, 2, 1]
            else:
                t_list = [32, 16, 8, 4, 2, 1]
            t_res = []
            c_list = combination(t_list, n)
            if c_list == []:
                c_list.append([])

            for i in range(len(c_list)):
                v = sum(c_list[i])
                if p == "h":
                    if v <= 11:
                        t_res.append(str(v) + ":")
                elif v <= 59:
                    t = str(v)
                    if v < 10:
                        t = "0" + t
                    t_res.append(t)
            return t_res

        if num == 0:
            return ["0:00"]
        h = 0
        while num - h > 5:
            h += 1

        res = []
        while h <= min(3,num):
            m = num - h
            h_list = all_time(h, "h")
            m_list = all_time(m, "m")
            for i in h_list:
                for j in m_list:
                    res.append(i + j)
            h += 1
        res.sort()
        return res

print(Solution().readBinaryWatch(2))
