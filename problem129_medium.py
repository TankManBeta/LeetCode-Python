# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/5 12:11
"""
"""
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：
例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。
叶节点 是指没有子节点的节点。

输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25

输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026
"""
"""
思路：首先看当前节点，为空就返回；然后看当前节点是否是叶子节点是叶子节点就求和，不是叶子节点就继续操作左子树和右子树，记得回溯
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.ans = 0

    def sum_numbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        combination = list()

        def get_ans(head):
            if not head:
                return
            combination.append(str(head.val))
            if not head.left and not head.right:
                self.ans += int(''.join(combination))
                return
            if head.left:
                get_ans(head.left)
                combination.pop()
            if head.right:
                get_ans(head.right)
                combination.pop()

        get_ans(root)
        return self.ans
