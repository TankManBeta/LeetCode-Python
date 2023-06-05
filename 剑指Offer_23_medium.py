# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/4 9:59
"""
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3
 
示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true
"""
"""
思路：根据二叉搜索树的定义，可以通过递归，判断所有子树的 正确性 （即其后序遍历是否满足二叉搜索树的定义） ，若所有子树都正确，
则此序列为二叉搜索树的后序遍历。递归终止条件： 当 i≥j ，说明此子树节点数量 ≤1 ，无需判别正确性，因此直接返回 true ；划分左右子树： 
遍历后序遍历的 [i,j] 区间元素，寻找 第一个大于根节点 的节点，索引记为 m 。此时，可划分出左子树区间 [i,m−1] 、右子树区间 [m,j−1] 、
根节点索引 j 。判断是否为二叉搜索树：左子树区间 [i,m−1] 内的所有节点都应 <postorder[j] 。而划分左右子树步骤已经保证左子树区间的
正确性，因此只需要判断右子树区间即可。右子树区间 [m,j−1] 内的所有节点都应 >postorder[j] 。实现方式为遍历，当遇到 ≤postorder[j] 
的节点则跳出；则可通过 p=j 判断是否为二叉搜索树。
"""


class Solution:
    @staticmethod
    def verifyPostorder(post_order: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while post_order[p] < post_order[j]:
                p += 1
            m = p
            while post_order[p] > post_order[j]:
                p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(post_order) - 1)
