class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        fastNode = dummyNode
        slowNode = dummyNode
        for i in range(n):
            fastNode = fastNode.next
        while fastNode.next:
            fastNode = fastNode.next
            slowNode = slowNode.next
        slowNode.next = slowNode.next.next
        return dummyNode.next