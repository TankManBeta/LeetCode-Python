# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/15 15:16
"""
from math import inf
from typing import Optional, List

"""
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

示例1：
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]

示例2：
输入: root = [1,2,3]
输出: [1,3]
"""
"""
思路：层次遍历，每次选择一层的最大值加入到ans中
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def largestValues(root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            max_val = -inf
            for node in queue:
                max_val = max(max_val, node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(max_val)
            queue = temp
        return res
