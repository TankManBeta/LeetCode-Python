# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/27 10:47
"""
"""
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
叶子节点 是指没有子节点的节点。

输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]

输入：root = [1]
输出：["1"]
"""
"""
思路：直接dfs，到叶子节点就在ans中添加结果
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.combinations = list()
        self.combination = list()

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def get_ans(head):
            if not head:
                return
            self.combination.append(str(head.val))
            if not head.left and not head.right:
                self.combinations.append("->".join(self.combination))
                return
            ways = []
            if head.left:
                ways.append(head.left)
            if head.right:
                ways.append(head.right)
            for way in ways:
                get_ans(way)
                self.combination.pop()

        get_ans(root)
        return self.combinations
