# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/30 10:24
"""
from typing import List

"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：[]

示例 3：
输入：root = [1,2], targetSum = 0
输出：[]
"""
"""
思路：dfs即可
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def pathSum(root: TreeNode, target: int) -> List[List[int]]:

        paths = []
        path = []

        def dfs(head, remain):
            if not head:
                return
            path.append(head.val)
            remain -= head.val
            if not head.left and not head.right and remain == 0:
                paths.append(path[:])
            dfs(head.left, remain)
            dfs(head.right, remain)
            path.pop()

        dfs(root, target)
        return paths
