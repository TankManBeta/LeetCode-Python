# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/2 9:40
"""
"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""
"""
思路：直接dfs即可
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(head, depth):
            if not head:
                self.ans = max(self.ans, depth)
                return
            dfs(head.left, depth + 1)
            dfs(head.right, depth + 1)

        dfs(root, 0)
        return self.ans
