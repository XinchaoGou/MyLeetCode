# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if (not (head and head.next)):
#             return head
#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return p

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while(curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
