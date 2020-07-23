import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        k,v = (collections.Counter(t) - collections.Counter(s)).popitem()
        return k

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord,t)) - sum(map(ord,s)))
