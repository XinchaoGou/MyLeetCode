class Solution:
    def countPrimes(self, n: int) -> int:
        i = 2
        isParime = [True] * (n+1)
        while(i*i < n+1):
            if(isParime[i]):
                for j in range(i*i,n+1,i):
                    isParime[j] = False
            i += 1
        return sum(isParime[2:-1])



input = 10
print(Solution().countPrimes(input))
