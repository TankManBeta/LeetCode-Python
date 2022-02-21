# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/20 11:13
"""
"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效二叉搜索树定义如下：
    节点的左子树只包含 小于 当前节点的数。
    节点的右子树只包含 大于 当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

输入：root = [2,1,3]
输出：true

输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
"""
"""
思路：中序遍历是一个升序序列
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def is_valid(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []

        def post_order(tree):
            if not tree:
                return
            post_order(tree.left)
            res.append(tree.val)
            post_order(tree.right)
        post_order(root)
        m = len(res)
        for i in range(m):
            if i+1 < m and res[i] >= res[i+1]:
                return False
        return True
