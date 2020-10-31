import collections
import random
class RandomizedCollection:
    def __init__(self):
        self.d = collections.defaultdict(set)
        self.v = []

    def insert(self, val: int) -> bool:
        self.d[val].add(len(self.v))
        self.v.append(val)
        return len(self.d[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.d[val]:
            return False
        i = self.d[val].pop()
        self.v[i] = self.v[-1]
        last = self.v.pop()
        self.d[last].discard(len(self.v))
        i < len(self.v) and self.d[last].add(i)
        return True

    def getRandom(self) -> int:
        return random.choice(self.v)


class RandomizedCollection:

    def __init__(self):
        self.d = collections.defaultdict(set)
        self.v = []

    def insert(self, val: int) -> bool:
        self.d[val].add(len(self.v))
        self.v.append(val)
        return len(self.d[val]) == 1


    def remove(self, val: int) -> bool:
        if not self.d[val]:
            return False
        # 用v的最后一个元素覆盖掉待移除元素
        idx = self.d[val].pop()
        self.v[idx] = self.v[-1]
        # 记录最后一个元素
        last_v = self.v.pop()
        # 从d中删除最后一个元素的最后角标, 因为已经pop了， 长度是原来len(v)-1
        self.d[last_v].discard(len(self.v))
        # 如果待删除元素已经是最后一个元素， 不用添加新idx角标，否则添加
        idx < len(self.v) and self.d[last_v].add(idx)
        return True

    def getRandom(self) -> int:
        return random.choice(self.v)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()