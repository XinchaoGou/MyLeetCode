# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        pre = None
        cur = second
        while cur:
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
        while pre and head:
            head_next = head.next
            pre_next = pre.next
            head.next = pre
            pre.next = head_next
            head = head_next
            pre = pre_next
        # return dummy.next