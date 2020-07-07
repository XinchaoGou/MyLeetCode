class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_par = {')':'(', '}':'{', ']':'['}
        flag = True
        for i in range(len(s)):
            current = s[i]
            if current in '([{':
                stack.append(current)
            else:
                if len(stack)>0 and valid_par.get(current) == stack[-1]:
                    stack.pop()
                else:
                    return False
        flag = True if len(stack) == 0 else False
        return flag
input = ']'
print(Solution().isValid(input))