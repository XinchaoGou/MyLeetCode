class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h_s = {}
        h_t = {}
        for i in range(len(s)):
            v_s = s[i]
            h_s[v_s] = h_s.get(v_s, 0) + 1
        for i in range(len(t)):
            v_t = t[i]
            h_t[v_t] = h_t.get(v_t, 0) + 1
        if len(h_s) != len(h_t):
            return False
        while h_s:
            k,v = h_s.popitem()
            if v != h_t.get(k,0):
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dicts[s[i]] = dicts.get(s[i], 0) + 1
            dicts[t[i]] = dicts.get(t[i],0) - 1
        if any(list(dicts.values())):
            return False
        return True