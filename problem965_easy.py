# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/5 22:24
"""
"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。

示例 1：
输入：[1,1,1,1,1,null,1]
输出：true

示例 2：
输入：[2,2,2,5,2]
输出：false
"""
"""
思路：我们可以对树进行一次深度优先搜索。当搜索到节点 x 时，我们检查 x 与 x 的每一个子节点之间的边是否满足要求。例如对于左子节点
而言，如果其存在并且值与 x 相同，那么我们继续向下搜索该左子节点；如果值与 x 不同，那么我们直接返回 False。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        if root.left:
            if root.val != root.left.val or not self.isUnivalTree(root.left):
                return False

        if root.right:
            if root.val != root.right.val or not self.isUnivalTree(root.right):
                return False

        return True
