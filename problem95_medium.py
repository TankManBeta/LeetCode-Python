# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/18 19:26
"""
"""
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

输入：n = 1
输出：[[1]]
"""
"""
思路：递归，枚举[start,end]中的值i为当前二叉搜索树的根，那么序列划分为了[start,i−1]和[i+1,end]两部分，我们递归调用这两部分，
获得所有可行的左子树和可行的右子树，那么最后一步我们只要从可行左子树集合中选一棵，再从可行右子树集合中选一棵拼接到根节点上，
并将生成的二叉搜索树放入答案数组即可。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def generate_trees(n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_trees(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree = TreeNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_trees.append(cur_tree)
            return all_trees

        return generate_trees(1, n) if n else []