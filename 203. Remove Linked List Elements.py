# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         if (head is None):
#             return None
#         l = head
#         while (l):
#             if l.val == val:
#                 l = l.next
#             else:
#                 head = l
#                 break
#         else:
#             return None
#
#         while (l and l.next):
#             if l.next.val == val:
#                 l.next = l.next.next
#             else:
#                 l = l.next
#         return head

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while(curr):
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next