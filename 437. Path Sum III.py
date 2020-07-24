# Definition for a binary tree node.
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
        node.left = TreeNode(m_list[i+1])
        node.right = TreeNode(m_list[i+2])
        layer.extend([node.left, node.right])
        i += 2
    return root

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, sumlist):
            if root is None: return 0
            sumlist = [num + root.val for num in sumlist] + [root.val]
            return sumlist.count(sum) + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return dfs(root, [])


tree = creat_tree([10,5,-3,3,2,None,11,3,-2,None,1])
sum_num = 8
Solution().pathSum(tree, sum_num)