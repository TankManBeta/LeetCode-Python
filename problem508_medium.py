# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/15 14:59
"""
from collections import Counter
from typing import List

"""
给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和
（不限顺序）。一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

示例 1：
输入: root = [5,2,-3]
输出: [2,-3,4]

示例 2：
输入: root = [5,2,-5]
输出: [2]
"""
"""
思路：用哈希表，求每个子树的和，cnt[sum]++，然后返回计数为maxCount的子树的和
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def findFrequentTreeSum(root: TreeNode) -> List[int]:
        cnt = Counter()

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            tmp_sum = node.val + dfs(node.left) + dfs(node.right)
            cnt[tmp_sum] += 1
            return tmp_sum

        dfs(root)

        maxCnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxCnt]
