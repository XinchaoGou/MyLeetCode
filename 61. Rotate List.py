# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not (head and head.next and k) :
            return head
        fast = head
        cnt = 1
        while fast.next:
            fast = fast.next
            cnt += 1
        fast.next = head
        slow = head
        for i in range(cnt - k%cnt - 1):
            slow = slow.next
        second = slow.next
        slow.next = None
        return second
