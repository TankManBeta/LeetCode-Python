# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/14 22:29
"""
from typing import Optional

"""
给你一个有 n 个结点的二叉树的根结点 root ，其中树中每个结点 node 都对应有 node.val 枚硬币。整棵树上一共有 n 枚硬币。
在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。移动可以是从父结点到子结点，
或者从子结点移动到父结点。
返回使每个结点上 只有 一枚硬币所需的 最少 移动次数。 

示例 1：
输入：root = [3,0,0]
输出：2
解释：一枚硬币从根结点移动到左子结点，一枚硬币从根结点移动到右子结点。

示例 2：
输入：root = [0,3,0]
输出：3
解释：将两枚硬币从根结点的左子结点移动到根结点（两次移动）。然后，将一枚硬币从根结点移动到右子结点。
"""
"""
思路：我们定义一个函数 dfs(node)，表示以 node 为根节点的子树中，金币的超载量，即金币的数量减去节点数。如果 dfs(node) 为正数，
表示该子树中金币的数量多于节点数，需要将多余的金币移出该子树；如果 dfs(node) 为负数，表示该子树中金币的数量少于节点数，需要
将不足的金币移入该子树。在函数 dfs(node) 中，我们首先遍历左右子树，获得左右子树的金币超载量 left 和 right。那么当前移动的次数
需要加上 ∣left∣+∣right∣，即将左右子树中的金币移动到当前节点。然后，我们返回整个子树的金币超载量，即 left+right+node.val−1。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def distributeCoins(root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            nonlocal ans
            ans += abs(left) + abs(right)
            return left + right + root.val - 1

        ans = 0
        dfs(root)
        return ans
