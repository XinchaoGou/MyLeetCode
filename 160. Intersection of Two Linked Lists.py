from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        searched_node = set()
        while (headA or headB):
            if (headA in searched_node):
                return headA
            if (headA):
                searched_node.add(headA)
                headA = headA.next

            if (headB in searched_node):
                return headB
            if (headB):
                searched_node.add(headB)
                headB = headB.next
        return None
# 双指针
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        while (pA or pB):
            if pA == pB:
                return pA
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return None