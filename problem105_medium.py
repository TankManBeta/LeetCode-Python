# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/23 14:53
"""
"""
给定两个整数数组preorder和inorder，其中preorder 是二叉树的先序遍历，inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。

输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

输入: preorder = [-1], inorder = [-1]
输出: [-1]
"""
"""
思路：先序遍历第一个节点是根节点，中序遍历当前根节点左边的属于左子树，右边的属于右子树，递归建树即可
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def build_tree(self, pre_order, in_order):
        """
        :type pre_order: List[int]
        :type in_order: List[int]
        :rtype: TreeNode
        """
        if not (pre_order and in_order):
            return None
        root = TreeNode(pre_order[0])
        mid_idx = in_order.index(pre_order[0])
        root.left = self.build_tree(pre_order[1:mid_idx + 1], in_order[:mid_idx])
        root.right = self.build_tree(pre_order[mid_idx + 1:], in_order[mid_idx + 1:])
        return root
