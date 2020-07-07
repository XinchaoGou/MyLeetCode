# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        if l1.val < l2.val:
            result = l1
            l1 = l1.next
        elif l2.val < l1.val:
            result = l2
            l2 = l2.next
        elif l1.val == l2.val:
            result = l1
            l1 = l1.next
            l2 = l2.next
        head.next = result
        while(l1.next is not None or l2.next is not None):
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            elif l2.val < l1.val:
                result.next = l2
                l2 = l2.next
            elif l1.val == l2.val:
                result.next = l1
                l1 = l1.next
                l2 = l2.next
        return head.next


l1_head = ListNode(0)
l1 = ListNode(1)
l1_head.next = l1
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(4)
l1 = l1_head.next

l2_head = ListNode(0)
l2 = ListNode(1)
l2_head.next = l2
l2.next = ListNode(3)
l2 = l2.next
l2.next = ListNode(4)
l2 = l2.next

a = Solution().mergeTwoLists(l1, l2)