# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convert(l, r):
            nonlocal head
            if l > r:
                return None

            mid = (l + r) // 2
            left = convert(l, mid - 1)
            root = TreeNode(head.val)
            root.left = left
            head = head.next
            right = convert(mid + 1, r)
            root.right = right
            return root

        ptr = head
        size = 0
        while ptr:
            ptr = ptr.next
            size += 1
        return convert(0, size - 1)