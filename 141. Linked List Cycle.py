# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pos = -1
        list_dict = {}
        idx = 0
        while(head and head.next):
            if head in list_dict:
                pos = list_dict[head]
                break
            list_dict[head] = idx
            idx += 1
            head = head.next
        return True if pos >= 0 else False

# 快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p_slow = head
        if head is None:
            return False
        p_fast = head.next
        res = False
        while (p_fast and p_fast.next):
            if p_slow == p_fast:
                res = True
                break
            p_slow = p_slow.next
            p_fast = p_fast.next.next
        return res
