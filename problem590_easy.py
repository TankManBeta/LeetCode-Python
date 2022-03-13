# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/12 15:20
"""
"""
给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

输入：root = [1,null,3,2,4,null,5,6]
输出：[5,6,3,2,4,1]

输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""
"""
思路：
（1）递归，首先访问孩子即可
（2）迭代，要是第一次访问就把孩子入栈，要是不是第一次访问就输入值即可
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    @staticmethod
    def post_order(root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # ans = []

        # def dfs(head):
        #     if not head:
        #         return
        #     for child in head.children:
        #         dfs(child)
        #     ans.append(head.val)

        # dfs(root)
        # return ans

        ans = []
        if not root:
            return ans
        my_stack = [root]
        visited = {}
        while my_stack:
            temp = my_stack[-1]
            is_visited = visited.get(temp, False)
            if is_visited:
                my_stack.pop()
                ans.append(temp.val)
                continue
            visited[temp] = True
            for i in range(len(temp.children) - 1, -1, -1):
                my_stack.append(temp.children[i])
        return ans
