# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/23 14:52
"""
"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
返回它的最大深度 3 。
"""
"""
思路：递归遍历即可
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

    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def get_depth(head, depth):
            if not head:
                self.ans = max(depth, self.ans)
                return
            get_depth(head.left, depth+1)
            get_depth(head.right, depth+1)
        get_depth(root, 0)
        return self.ans
