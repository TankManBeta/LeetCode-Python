# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/3 10:08
"""
"""
路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中至多出现一次 。
该路径至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和 。

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
"""
"""
思路：计算左右分支最大值，如果分支为负数还不如不选择，计算路径与已经计算过历史最大值做比较，返回经过root的单边最大分支给当前
root的父节点计算使用
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_path_value = float("-inf")

    def max_path_sum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_value(node):
            if not node:
                return 0
            left_max_value = max(max_value(node.left), 0)
            right_max_value = max(max_value(node.right), 0)
            path_value = node.val + left_max_value + right_max_value
            self.max_path_value = max(path_value, self.max_path_value)
            return node.val + max(left_max_value, right_max_value)

        max_value(root)
        return self.max_path_value
