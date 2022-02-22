# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/21 14:29
"""
"""
给你二叉树的根节点root，返回其节点值的层序遍历。 （即逐层地，从左到右访问所有节点）。

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

输入：root = [1]
输出：[[1]]

输入：root = []
输出：[]
"""
"""
思路：层次遍历用队列，每次统计当前队列的长度就是每一层的节点个数，然后加进这一层的res即可
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def level_order(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        res = []
        if not root:
            return res
        queue.append(root)
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
            res.append(temp_res)
        return res
