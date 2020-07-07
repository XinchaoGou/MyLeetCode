class Solution:
    def plusOne(self, digits):
        i = 1
        dig_len = len(digits)
        while (i <= dig_len):
            t_dig = digits[-i]
            if t_dig == 9:
                digits[-i] = 0
                i += 1
            else:
                digits[-i] += 1
                break
        if digits[0] == 0:
            digits.insert(0,1)
        return digits

input = [1,2,3,4]
print(Solution().plusOne(input))
