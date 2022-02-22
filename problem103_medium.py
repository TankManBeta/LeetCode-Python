# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/21 15:12
"""
"""
给你二叉树的根节点root，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]

输入：root = [1]
输出：[[1]]

输入：root = []
输出：[]
"""
"""
思路：在102题的基础之上记录一下层次的奇偶
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def zigzag_level_order(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        res = []
        if not root:
            return res
        queue.append(root)
        k = 0
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
            if k % 2 == 0:
                res.append(temp_res)
            else:
                res.append(temp_res[::-1])
            k += 1
        return res
