class Solution:
    def countSegments(self, s: str) -> int:
        cnt = 0
        word = 0
        for c in s:
            if c != " ":
                if word == 0:
                    cnt += 1
                word += 1
            else:
                word = 0
        return cnt