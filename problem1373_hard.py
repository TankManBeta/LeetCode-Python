# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/20 12:58
"""
from math import inf
from typing import Optional

"""
给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。
二叉搜索树的定义如下：
    任意节点的左子树中的键值都 小于 此节点的键值。
    任意节点的右子树中的键值都 大于 此节点的键值。
    任意节点的左子树和右子树都是二叉搜索树。

示例 1：
输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
输出：20
解释：键值为 3 的子树是和最大的二叉搜索树。

示例 2：
输入：root = [4,3,null,1,2]
输出：2
解释：键值为 2 的单节点子树是和最大的二叉搜索树。

示例 3：
输入：root = [-4,-2,-5]
输出：0
解释：所有节点键值都为负数，和最大的二叉搜索树为空。

示例 4：
输入：root = [2,1,3]
输出：6

示例 5：
输入：root = [5,4,8,3,null,6,3]
输出：7
"""
"""
思路：
判断一棵树是否是二叉搜索树，需要满足以下四个条件：
    左子树是二叉搜索树；
    右子树是二叉搜索树；
    左子树的最大值小于根节点的值；
    右子树的最小值大于根节点的值。
因此，我们设计一个函数 dfs(root)，函数的返回值是一个四元组 (bst,mi,mx,s)，其中：数字 bst 表示以 root 为根的树是否是二叉搜索树。
如果是二叉搜索树，则 bst=1；否则 bst=0；数字 mi 表示以 root 为根的树的所有节点的最小值；数字 mx 表示以 root 为根的树的所有节点
的最大值；数字 s 表示以 root 为根的树的所有节点的和。
函数 dfs(root) 的执行逻辑如下：
如果 root 为空节点，则返回 (1,+∞,−∞,0)，表示空树是二叉搜索树，最小值和最大值分别为正无穷和负无穷，节点和为 0。
否则，递归计算 root 的左子树和右子树，分别得到 (lbst,lmi,lmx,ls) 和 (rbst,rmi,rmx,rs)，然后判断 root 节点是否满足二叉搜索树的条件：
    如果满足 lbst=1 且 rbst=1 且 lmx<root.val<rmi，则以 root 为根的树是二叉搜索树，节点和 s=ls+rs+root.val。我们更新答案 
    ans=max(ans,s)，并返回 (1,min(lmi,root.val),max(rmx,root.val),s)。
    否则，以 root 为根的树不是二叉搜索树，我们返回 (0,0,0,0)。
我们在主函数中调用 dfs(root)，执行完毕后，答案即为 ans。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def maxSumBST(root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> tuple:
            if root is None:
                return 1, inf, -inf, 0
            lbst, lmi, lmx, ls = dfs(root.left)
            rbst, rmi, rmx, rs = dfs(root.right)
            if lbst and rbst and lmx < root.val < rmi:
                nonlocal ans
                s = ls + rs + root.val
                ans = max(ans, s)
                return 1, min(lmi, root.val), max(rmx, root.val), s
            return 0, 0, 0, 0

        ans = 0
        dfs(root)
        return ans
