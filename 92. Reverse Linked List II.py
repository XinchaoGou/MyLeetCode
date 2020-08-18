# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        # pre 和 cur 用来翻转链表
        pre, cur = dummy, head
        # left 和 pre_left 用来记录左边截断的两个节点
        left, pre_left = None, None
        cnt = 1
        while pre:
            # 1. 如果没达到m往后遍历即可，达到的时候，记录截断点
            if cnt <= m:
                if cnt == m:
                    pre_left = pre
                    left = cur
                cur = cur.next
                pre = pre.next
            # 2. 如果是达到n了整段翻转
            elif cnt > n:
                pre_left.next = pre
                left.next = cur
                break
            # 3. 如果是m到n之间，翻转链表
            else:
                cur_next = cur.next
                cur.next = pre
                pre = cur
                cur = cur_next
            cnt += 1
        return dummy.next