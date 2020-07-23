class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        res =""
        cnt_A = 0
        cnt_B = 0
        array = [0] * 10
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            if  s == g:
                cnt_A += 1
            else:
                array[s] += 1
                array[g] -= 1
        cnt_B = len(secret) - cnt_A - sum(list(filter(lambda x: x > 0, array)))

        return str(cnt_A)+"A" + str(cnt_B) +"B"