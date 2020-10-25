# 栈
class Solution:
    def decodeString(self, s: str) -> str:
        cnt = ''
        res = ''
        stack = []
        cnt_stack = []
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                cnt += c
            elif c == '[':
                cnt_stack.append(int(cnt))
                cnt = ''
                stack.append(res)
                res = ''
            elif c == ']':
                m_cnt = cnt_stack.pop()
                last_res = stack.pop()
                res = last_res + res * m_cnt
            else:
                res += c
        return res

class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cnt_stack = []
        cnt = ''
        s = list(s)
        i = 0
        while i < len(s):
            c = s[i]
            if c  == '[':
                stack.append(i)
                cnt_stack.append(cnt)
                cnt = ''
            elif c == ']':
                start = stack.pop()
                cnt = cnt_stack.pop()
                end = i
                word = s[start+1:end]

                s[start - len(cnt):end+1] = word*int(cnt)
                diff = len(word)*int(cnt) - (end+1 - start + len(cnt))
                i += diff
                cnt = ''
            elif c.isdigit():
                cnt += c
            i += 1
        return ''.join(s)

s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))