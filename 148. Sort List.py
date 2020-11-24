# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def creat_list(m_list):
    if m_list == []:
        return None
    head = ListNode(m_list[0])
    cur_node = head
    for i in range(1, len(m_list)):
        cur_node.next = ListNode(m_list[i])
        cur_node = cur_node.next
    return head

def print_list(m_list):
    while m_list:
        if m_list is None:
            return
        else:
            print(m_list.val)
            m_list = m_list.next


# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         def merge(left_head, right_head):
#             if left_head is None or right_head is None:
#                 return left_head or right_head
#             if left_head.val > right_head.val:
#                 left_head, right_head = right_head, left_head
#             result = left_head
#             cur_node = left_head
#             left_head = left_head.next
#             while left_head and right_head:
#                 if left_head.val <= right_head.val:
#                     cur_node.next = left_head
#                     left_head = left_head.next
#                 else:
#                     cur_node.next = right_head
#                     right_head = right_head.next
#                 cur_node = cur_node.next
#             cur_node.next = left_head or right_head
#             return result

#         if head is None or head.next is None:
#             return head

#         slow = head
#         fast = head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         second = slow.next
#         slow.next = None
#         left = self.sortList(head)
#         right = self.sortList(second)
#         return merge(left, right)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(first, second):
            if first is None or second is None:
                return first or second
            if first.val > second.val:
                first, second = second, first

            res = first
            cur = first
            first = first.next
            while first and second:
                if first.val < second.val:
                    cur.next = first
                    first = first.next
                else:
                    cur.next = second
                    second = second.next
                cur = cur.next
            cur.next = first or second
            return res

        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        first = self.sortList(head)
        second = self.sortList(second)
        return merge(first, second)

input = creat_list([4, 2, 1, 3])
outout = Solution().sortList(input)
print_list(outout)
