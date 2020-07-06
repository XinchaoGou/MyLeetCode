from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search_helper(p, cur_idx):
            (y, x) = p
            if p in searched_area:
                return False
            boundary_cond = x >= 0 and x < m and y >= 0 and y < n
            if boundary_cond and board[y][x] == word[cur_idx]:
                searched_area.append((y, x))
                if cur_idx == len(word) - 1:
                    return True
                elif search_helper((y - 1, x), cur_idx + 1) \
                           or search_helper((y + 1, x), cur_idx + 1) \
                           or search_helper((y, x - 1), cur_idx + 1) \
                           or search_helper((y, x + 1), cur_idx + 1):
                    return True
                else:
                    if searched_area != []:
                        searched_area.pop()
            return False

        if word == '':
            return True

        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                searched_area = []
                if search_helper((i, j), 0):
                    return True
        return False


input_board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]]


word = "ABCB"
output = Solution().exist(input_board, word)
print(output)
