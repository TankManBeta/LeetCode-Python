# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/19 16:53
"""
"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

输入：p = [1,2,3], q = [1,2,3]
输出：true

输入：p = [1,2], q = [1,null,2]
输出：false

输入：p = [1,2,1], q = [1,1,2]
输出：false
"""
"""
思路：比较当前节点和当前节点的左右子树
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def is_same_tree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
