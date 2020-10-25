# 回溯法
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backTrack(i):
            nonlocal col_set, lc_set, rc_set, cnt
            for j in range(n):
                if j not in col_set and (i-j) not in lc_set and (i+j) not in rc_set:
                    if i == n-1:
                        cnt += 1
                        return
                    col_set.add(j)
                    lc_set.add(i-j)
                    rc_set.add(i+j)

                    backTrack(i+1)

                    col_set.discard(j)
                    lc_set.discard(i-j)
                    rc_set.discard(i+j)

        col_set = set()
        lc_set = set()
        rc_set = set()
        cnt = 0
        backTrack(0)
        return cnt

# 位元算
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backTrack(row, col, diag1, diag2):
            if row == n:
                return 1
            else:
                cnt = 0
                all_positions = ((1<<n) - 1) & (~(col|diag1|diag2))
                while all_positions:
                    position = all_positions & (-all_positions)
                    all_positions &= (all_positions - 1)
                    cnt += backTrack(row+1,col|position, (diag1|position)<<1, (diag2|position)>>1)
                return cnt

        return backTrack(0, 0, 0, 0)
print(Solution().totalNQueens(4))