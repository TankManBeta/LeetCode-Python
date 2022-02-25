# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/24 15:16
"""
"""
给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

输入：root = [3,9,20,null,null,15,7]
输出：[[15,7],[9,20],[3]]

输入：root = [1]
输出：[[1]]

输入：root = []
输出：[]
"""
"""
思路：同102，只是把插入位置从最后放到了最前
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def level_order_bottom(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        res = []
        if not root:
            return res
        queue.append(root)
        while queue:
            temp_res = []
            size = len(queue)
            for i in range(0, size):
                temp_node = queue.pop(0)
                temp_res.append(temp_node.val)
                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
            res.insert(0, temp_res)
        return res
