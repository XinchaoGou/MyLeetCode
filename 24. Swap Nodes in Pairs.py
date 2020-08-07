class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (not head or not head.next):
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        slow = dummyNode
        fast = head.next

        while (fast):
            next_slow = slow.next
            next_fast = fast.next.next if fast.next else None

            slow.next.next = fast.next
            fast.next = slow.next
            slow.next = fast

            slow = next_slow
            fast = next_fast
        return dummyNode.next