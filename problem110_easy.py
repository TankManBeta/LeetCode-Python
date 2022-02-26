# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/25 15:02
"""
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1 。

输入：root = [3,9,20,null,null,15,7]
输出：true

输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

输入：root = []
输出：true
"""
"""
思路：
（1）计算左右两棵子树的高度，看左右两个树是否是高度平衡二叉树
（2）当节点root左/右子树的高度差<2，则返回以节点root为根节点的子树的最大高度，即节点root的左右子树中最大高度加1；当节点root
左/右子树的高度差≥2。则返回−1，代表此子树不是平衡树。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    @staticmethod
    def is_balanced(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def height(root):
        #     if not root:
        #         return 0
        #     return max(height(root.left), height(root.right)) + 1
        # if not root:
        #     return True
        # return abs(height(root.left) - height(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

        def height(head):
            if not head:
                return 0
            left_height = height(head.left)
            if left_height == -1:
                return -1
            right_height = height(head.right)
            if right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1

        return height(root) >= 0
