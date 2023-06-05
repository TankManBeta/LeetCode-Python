# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/4 8:46
"""
from typing import List

"""
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 

示例 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

示例 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""
"""
思路：先序遍历的第一个节点是根节点，然后在中序遍历中找到根节点的索引，分成左右两个子树。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def buildTree(pre_order: List[int], in_order: List[int]) -> TreeNode:
        def recur(root, left, right):
            if left > right:
                return  # 递归终止
            node = TreeNode(pre_order[root])  # 建立根节点
            i = dic[pre_order[root]]  # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)  # 开启左子树递归
            node.right = recur(i - left + root + 1, i + 1, right)  # 开启右子树递归
            return node  # 回溯返回根节点

        dic, pre_order = {}, pre_order
        for i in range(len(in_order)):
            dic[in_order[i]] = i
        return recur(0, 0, len(in_order) - 1)
