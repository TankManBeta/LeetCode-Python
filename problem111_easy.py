# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/25 11:01
"""
"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

输入：root = [3,9,20,null,null,15,7]
输出：2

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
"""
"""
思路：左子树为空，最小距离就是右子树深度+1；右子树为空，最小距离就是左子树深度+1；否则就是左右子树最小深度+1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def min_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 0
        # elif not root.left:
        #     return self.minDepth(root.right) + 1
        # elif not root.right:
        #     return self.minDepth(root.left) + 1
        # else:
        #     return min(self.minDepth(root.left), self.minDepth(root.right))+1

        if not root:
            return 0
        l_depth = self.min_depth(root.left)
        r_depth = self.min_depth(root.right)
        return l_depth + r_depth + 1 if l_depth * r_depth == 0 else min(l_depth, r_depth) + 1
