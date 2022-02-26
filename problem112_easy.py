# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/25 15:17
"""
"""
给你二叉树的根节点root和一个表示目标和的整数targetSum。判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于
目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
叶子节点 是指没有子节点的节点。

输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。

输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。

输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。
"""
"""
思路：如果是叶子节点就判断是否满足条件，否则继续判断左子树和右子树
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def has_path_sum(self, root, target_sum):
        """
        :type root: TreeNode
        :type target_sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return target_sum == root.val
        return self.has_path_sum(root.left, target_sum-root.val) or self.has_path_sum(root.right, target_sum-root.val)
