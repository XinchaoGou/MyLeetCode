# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def creat_list(input_list:list):
    head = ListNode(0)
    l = head
    for i in range(len(input_list)):
        l.next = ListNode(input_list[i])
        l = l.next
    return head.next

def print_list(output_list:ListNode):
    while(output_list != None):
        print(output_list.val)
        output_list = output_list.next




class Solution:
    # 官方
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l = head
        while(l != None and l.next != None):
            if(l.val == l.next.val):
                l.next = l.next.next
            else:
                l = l.next
        return head

    # 官方改进
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     l = head
    #     if head is None:
    #         return head
    #     pre_v = l.val
    #     while(l != None and l.next != None):
    #         if(pre_v == l.next.val):
    #             l.next = l.next.next
    #         else:
    #             l = l.next
    #             pre_v = l.val
    #     return head

    # 我的
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if head is None:
    #         return head
    #     l = head
    #     pre_v = l.val
    #
    #     l_next = l.next
    #     while (not (l_next is None)):
    #         if(l_next.val == pre_v):
    #             l_next = l_next.next
    #         else:
    #             l.next = l_next
    #             l = l.next
    #             l_next = l.next
    #             pre_v = l.val
    #     l.next = l_next
    #     return head


# input = ListNode(1)
# input_head = input
# input.next = ListNode(1)
# input = input.next
# input.next = ListNode(1)
# input = input.next
# input.next = ListNode(2)
# input = input.next
# input.next = ListNode(3)
# input = input.next
# input.next = ListNode(3)
# input_head = None

input_head = creat_list([1,2,3])
output = Solution().deleteDuplicates(input_head)
print_list(output)