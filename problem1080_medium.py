# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/22 9:51
"""
from typing import Optional

"""
给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。
假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。
叶子节点，就是没有子节点的节点。 

示例 1：
输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
输出：[1,2,3,4,null,null,7,8,9,null,14]

示例 2：
输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
输出：[5,4,8,11,null,17,4,7,null,null,null,5]

示例 3：
输入：root = [1,2,-3,-5,null,4,null], limit = -1
输出：[1,null,-3,4]
"""
"""
思路：递归。如果 root 为空，那么返回空；否则，我们将 limit 减去当前节点的值，即 limit=limit−root.val，然后继续执行下述步骤。
如果 root 为叶子节点（即 root 的左右子节点都为空），说明我们已经走完了一条从根节点到叶子节点的路径。如果此时 limit>0，说明
该路径上所有节点的值的和小于 limit，我们返回空节点，表示删除；否则，说明该路径上所有节点的值的和大于等于 limit，我们返回 root。
如果 root 不是叶子节点，那么我们递归调用函数 sufficientSubset，对 root 的左右子节点分别进行处理，并将返回值分别赋值给 root 
的左右子节点。如果 root 的左右子节点在经过递归调用后变成了空节点，那么说明 root 的左右子树中所有从根节点到叶子节点的路径上所有
节点的值的和都小于 limit，因此我们返回空节点，表示删除 root；否则，说明 root 的左右子树中存在从根节点到叶子节点上所有节点值的和
大于等于 limit 的路径，返回 root。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(
            self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        if root is None:
            return None
        limit -= root.val
        if root.left is None and root.right is None:
            return None if limit > 0 else root
        root.left = self.sufficientSubset(root.left, limit)
        root.right = self.sufficientSubset(root.right, limit)
        return None if root.left is None and root.right is None else root
