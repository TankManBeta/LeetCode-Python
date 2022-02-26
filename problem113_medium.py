# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/25 15:36
"""
"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

输入：root = [1,2], targetSum = 0
输出：[]
"""
"""
思路：同112，只需要记住路径并恢复原来的状态即可
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def path_sum(root, target_sum):
        """
        :type root: TreeNode
        :type target_sum: int
        :rtype: List[List[int]]
        """
        combination = list()
        combinations = list()

        def dfs(head, target):
            if not head:
                return
            combination.append(head.val)
            if not head.left and not head.right:
                if target == head.val:
                    combinations.append(combination[:])
            dfs(head.left, target-head.val)
            dfs(head.right, target-head.val)
            combination.pop()
        dfs(root, target_sum)
        return combinations
