# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/19 0:06
"""
"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

输入：root = [1,null,2,3]
输出：[1,3,2]

输入：root = []
输出：[]

输入：root = [1]
输出：[1]

输入：root = [1,2]
输出：[2,1]

输入：root = [1,null,2]
输出：[1,2]
"""
"""
思路：左子树不为空时，遍历先左子树，然后右子树
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def in_order_traversal(head):
        """
        :type head: TreeNode
        :rtype: List[int]
        """
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(head)
        return res
