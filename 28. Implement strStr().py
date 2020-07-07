class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        if (n_len == 0):
            return 0
        if n_len > h_len:
            return -1

        n_jump = [0] * n_len
        i = 2
        i_p = i - 1
        s_p = 0
        cnt = 0
        while(i < n_len):
            if (needle[i_p] == needle[s_p]):
                if (i_p == i-1):
                    n_jump[i] = s_p + 1
                    i += 1
                s_p += 1
                i_p += 1
            elif (s_p == 0):
                n_jump[i] = 0
                i += 1
                i_p += 1
            else:
                i_p -= s_p - 1
                s_p = 0
            cnt += 1
            print(cnt, i_p, s_p, n_jump)

        # print(n_jump)
        sub_p = 0
        i = 0
        while (i < h_len):
            # print(haystack[i] , needle[sub_p] , sub_p)
            if (haystack[i] == needle[sub_p]):
                if (sub_p == n_len - 1):
                    return i - sub_p
                sub_p += 1
                i += 1
            elif (sub_p == 0):
                i += 1
            else:
                sub_p = n_jump[sub_p]
        return -1

#
# haystack = "mississippi"
# needle = "issip"
haystack = "aabaaabaaac"
needle = 'aaaaaaaabc'
# needle = "aabaaac"
# haystack ="bbababaaaababbaabbbabbbaaabbbaaababbabaabbaaaaabbaaabbbbaaabaabbaababbbaabaaababbaaabbbbbbaabbbbbaaabbababaaaaabaabbbababbaababaabbaa"
# needle ="bbabba"
# haystack = "a"
# needle = "a"
print(Solution().strStr(haystack, needle))
