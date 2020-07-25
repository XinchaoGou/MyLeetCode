from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        cur_c = chars[0]
        cur_cnt = 0
        sum_cnt = 0
        length = len(chars)
        for i in range(length):
            c = chars[i]
            if c == cur_c:
                cur_cnt += 1
            else:
                chars[sum_cnt] = cur_c
                sum_cnt += 1
                if cur_cnt > 1:
                    for digit in list(str(cur_cnt)):
                        chars[sum_cnt] = digit
                        sum_cnt += 1
                cur_c = c
                cur_cnt = 1
            if i == length - 1:
                chars[sum_cnt] = cur_c
                sum_cnt += 1
                if cur_cnt > 1:
                    for digit in list(str(cur_cnt)):
                        chars[sum_cnt] = digit
                        sum_cnt += 1
        return sum_cnt

class Solution(object):
    def compress(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write