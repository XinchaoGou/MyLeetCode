from typing import List
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 顺序合并
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2Lists(a, b):
            if not a or not b:
                return a or b
            head = ListNode()
            p = head
            while a and b:
                if a.val < b.val:
                    p.next = a
                    a = a.next
                else:
                    p.next = b
                    b = b.next
                p = p.next
            p.next = a or b
            return head.next

        if not lists:
            return None
        res = lists[0]
        for i in range(1, len(lists)):
            res = merge2Lists(res, lists[i])
        return res

# 分治合并
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2List(a,b):
            if not a or not b:
                return a or b
            head = ListNode()
            p = head
            while a and b:
                if a.val < b.val:
                    p.next = a
                    a = a.next
                else:
                    p.next = b
                    b = b.next
                p = p.next
            p.next = a or b
            return head.next

        if not lists:
            return None
        gap = 1
        n = len(lists)
        while gap < n:
            for i in range(0, n, gap*2):
                if i + gap < n:
                    lists[i] = merge2List(lists[i], lists[i+gap])
            gap *= 2
        return lists[0]

# 优先队列 （堆）
ListNode.__lt__ = lambda a, b: a.val < b.val
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hpq = []
        for i in range(len(lists)):
            node =lists[i]
            if node: heapq.heappush(hpq, node)
        head = ListNode()
        p = head
        while hpq:
            node = heapq.heappop(hpq)
            p.next = node
            p = p.next
            node = node.next
            if node: heapq.heappush(hpq, node)
        return head.next