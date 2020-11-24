# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def creat_tree(m_list):
    if m_list == []:
        return None
    root = TreeNode(m_list[0])
    layer = [root]
    i = 0
    while layer:
        node = layer.pop(0)
        if i >= len(m_list) - 1:
            break
        if m_list[i+1] is not None:
            node.left = TreeNode(m_list[i+1])
            layer.append(node.left)
        if m_list[i+2] is not None:
            node.right = TreeNode(m_list[i+2])
            layer.append(node.right)
        i += 2
    return root


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def creat_list(input_list: list):
    head = ListNode(0)
    l = head
    for i in range(len(input_list)):
        l.next = ListNode(input_list[i])
        l = l.next
    return head.next


def print_list(output_list: ListNode):
    while(output_list != None):
        print(output_list.val)
        output_list = output_list.next
