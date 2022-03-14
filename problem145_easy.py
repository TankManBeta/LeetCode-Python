# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/13 16:01
"""
"""
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

输入：root = [1,null,2,3]
输出：[3,2,1]

输入：root = []
输出：[]

输入：root = [1]
输出：[1]
"""
"""
思路：
（1）直接递归
（2）迭代，需要记录前驱节点
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def post_order_traversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # self.ans = []

        # def post_order(head):
        #     if not head:
        #         return
        #     post_order(head.left)
        #     post_order(head.right)
        #     self.ans.append(head.val)

        # post_order(root)
        # return self.ans

        if not root:
            return list()
        res = list()
        stack = list()
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res
