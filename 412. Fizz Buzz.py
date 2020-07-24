from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            v = i
            if i % 3 == 0 and i % 5 == 0:
                v = "FizzBuzz"
            elif i % 3 == 0:
                v = "Fizz"
            elif i % 5 == 0:
                v = "Buzz"
            else:
                v = str(v)
            res.append(v)
        return res