# 中心拓展
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            cnt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                cnt += 1
            return cnt

        if len(s) == 0:
            return 0
        res = 1
        for i in range(1, len(s)):
            res += expand(i, i) + expand(i - 1, i)
        return res

# 马拉车
class Solution:
    def countSubstrings(self, s: str) -> int:
        ts = '$' + s.replace('', '#') + '!'
        d,Im,r,ans= [0]*(len(ts)-2),0,0,0
        for i in range(2, len(ts)-2):
            if(i<=r):#当对称中心i被包含在当前最大回文串内时，拓展过程可以加速
                d[i]=min(d[2 * Im - i],r - i )
            while (ts[i - d[i]-1] == ts[i + d[i]+1]):#满足条件，向左右拓展半径
                d[i] += 1
            if i + d[i] > r:
                Im, r = i, i + d[i]
            ans += (d[i]+1)//2
        return ans

s = "aaa"
print(Solution().countSubstrings(s))