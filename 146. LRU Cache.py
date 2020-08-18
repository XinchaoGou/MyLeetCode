import collections

class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dummy_head = DLinkedNode()
        self.dummy_tail = DLinkedNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            if len(self.cache) > self.capacity:
                self.del_tail()
        else:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)

    def del_tail(self):
        old_tail = self.dummy_tail.pre
        new_tail = old_tail.pre
        new_tail.next = self.dummy_tail
        self.dummy_tail.pre = new_tail
        self.cache.pop(old_tail.key)

    def add_to_head(self, node: DLinkedNode):
        old_head = self.dummy_head.next
        self.dummy_head.next = node
        node.pre = self.dummy_head
        node.next = old_head
        old_head.pre = node

    def move_to_head(self, node: DLinkedNode):
        node_pre = node.pre
        node_next = node.next
        node_pre.next = node_next
        node_next.pre = node_pre
        self.add_to_head(node)
