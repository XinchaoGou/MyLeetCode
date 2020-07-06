class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     n_str =[i for i in bin(n)[2:] if i == '1']
    #     return len(n_str)
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while( n != 0):
            n &= n-1
            sum += 1
        return sum


input = int('11111111111111111111111111111101',2)
print(Solution().hammingWeight(input))