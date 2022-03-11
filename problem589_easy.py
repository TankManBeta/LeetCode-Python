# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/10 9:57
"""
"""
给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

输入：root = [1,null,3,2,4,null,5,6]
输出：[1,3,5,6,2,4]

输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""
"""
思路：
（1）直接递归即可
（2）迭代，每次访问弹出当前节点，并把当前节点的孩子节点逆序进栈
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def __init__(self):
        self.ans = []

    def pre_order(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # def traverse(head):
        #     if not head:
        #         return
        #     self.ans.append(head.val)
        #     for child in head.children:
        #         traverse(child)
        # traverse(root)
        # return self.ans

        if root is None:
            return []
        ans = []
        st = [root]
        while st:
            node = st.pop()
            ans.append(node.val)
            st.extend(reversed(node.children))
        return ans
