# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not (head and head.next):
            return True
        slow = head
        fast = head.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        pre = None
        cur = second
        while (cur):
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
        while(pre and head):
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True