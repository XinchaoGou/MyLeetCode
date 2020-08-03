from math import sqrt
from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        M = int(sqrt(area))
        L = area // M
        while L*M - area:
            M -= 1
            L = area //M
        return [L,M]