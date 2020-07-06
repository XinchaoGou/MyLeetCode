# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_merged = ListNode(0)
        l_head = l_merged
        while (l1 and l2):
            if (l1.val <= l2.val):
                l_merged.next = l1
                l1 = l1.next
            else:
                l_merged.next = l2
                l2 = l2.next
            l_merged = l_merged.next

        if (l1 is None):
            l_merged.next = l2
        elif (l2 is None):
            l_merged.next = l1
        return l_head.next


l1 = ListNode(1)
l1_haed = l1
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(4)
l1 = l1_haed

l2 = ListNode(1)
l2_head = l2
l2.next = ListNode(3)
l2 = l2.next
l2.next = ListNode(4)
l2 = l2.next
l2 = l2_head

output = Solution().mergeTwoLists(l1, l2)
print(output)
