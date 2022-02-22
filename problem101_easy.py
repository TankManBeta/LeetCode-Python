# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/21 15:06
"""
"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

输入：root = [1,2,2,3,4,4,3]
输出：true

输入：root = [1,2,2,null,3,null,3]
输出：false
"""
"""
思路：判断当前值是否相等以及当前的左子树和另一棵树的右子树以及当前的右子树和另一棵树的左子树是否对称
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def is_symmetric(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        if not root:
            return True
        return check(root.left, root.right)
