# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/30 11:02
"""
from typing import Optional, List

"""
给出二叉树的根节点 root，树上每个节点都有一个不同的值。
如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
返回森林中的每棵树。你可以按任意顺序组织答案。 

示例 1：
输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]

示例 2：
输入：root = [1,2,4,null,3], to_delete = [3]
输出：[[1,2,4]]
"""
"""
思路：更新左儿子（右儿子）为递归左儿子（右儿子）的返回值。如果当前节点被删除，那么就检查左儿子（右儿子）是否被删除，如果没被删除，
就加入答案。如果当前节点被删除，返回空节点，否则返回当前节点。最后，如果根节点没被删除，把根节点加入答案。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def delNodes(root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        s = set(to_delete)

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            # 当前节点没被删，返回自身
            if node.val not in s:
                return node
            # 当前节点被删了，左右子树如果存在就加入答案
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            # 当前节点被删了返回None
            return None

        if dfs(root):
            ans.append(root)
        return ans
