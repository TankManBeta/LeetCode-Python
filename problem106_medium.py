# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/23 14:57
"""
"""
给定两个整数数组inorder和postorder，其中inorder是二叉树的中序遍历，postorder是同一棵树的后序遍历，请你构造并返回这颗二叉树。

输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]

输入：inorder = [-1], postorder = [-1]
输出：[-1]
"""
"""
思路：后序遍历的最后一个节点是根节点，中序遍历中根节点的左边属于左子树，根节点的右边属于右子树，递归建树即可
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def build_tree(self, in_order, post_order):
        """
        :type in_order: List[int]
        :type post_order: List[int]
        :rtype: TreeNode
        """
        if not (post_order and in_order):
            return None
        root = TreeNode(post_order[-1])
        index = in_order.index(post_order[-1])
        root.left = self.build_tree(in_order[0:index], post_order[:index])
        root.right = self.build_tree(in_order[index + 1:], post_order[index:-1])
        return root
