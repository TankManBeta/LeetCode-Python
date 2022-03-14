# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/13 15:45
"""
"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

输入：root = [1,null,2,3]
输出：[1,2,3]

输入：root = []
输出：[]

输入：root = [1]
输出：[1]

输入：root = [1,2]
输出：[1,2]

输入：root = [1,null,2]
输出：[1,2]
"""
"""
思路：
（1）直接递归
（2）迭代，有左子树就一直遍历左子树，让其进队，然后右子树
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def pre_order_traversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # self.ans = []

        # def pre_order(head):
        #     if not head:
        #         return
        #     self.ans.append(head.val)
        #     pre_order(head.left)
        #     pre_order(head.right)

        # pre_order(root)
        # return self.ans

        ans = []
        if not root:
            return ans
        stack = []
        node = root
        while stack or node:
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return ans
