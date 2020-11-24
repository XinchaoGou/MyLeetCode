#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

import leetcode
from leetcode import ListNode
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        lastSorted = head
        cur = head.next

        while cur:
            if lastSorted.val <= cur.val:
                lastSorted = cur
            else:
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                lastSorted.next = cur.next
                cur.next =prev.next
                prev.next = cur
            cur = lastSorted.next
        return dummy.next

# @lc code=end

# 我的代码
# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         dummy = ListNode(float('-inf'))
#         dummy.next = head

#         while head:
#             head_next = head.next
#             head.next = None
#             cur = dummy.next
#             pre = dummy
#             while cur and cur.val < head.val:
#                 cur = cur.next
#                 pre = pre.next
#             if cur != head:
#                 pre.next = head
#                 head.next = cur
#             head = head_next
#         return dummy.next

head = leetcode.creat_list([-1, 5, 3, 4, 0])
leetcode.print_list(Solution().insertionSortList(head))
