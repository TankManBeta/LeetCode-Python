# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/10 15:44
"""
from typing import Optional

"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
    首先找到需要删除的节点；
    如果找到了，删除它。
    
示例 1:
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。

示例 2:
输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点

示例 3:
输入: root = [], key = 0
输出: []
"""
"""
思路：
如果 root 为空，代表未搜索到值为 key 的节点，返回空。
如果 root.val>key，表示值为 key 的节点可能存在于 root 的左子树中，需要递归地在 root.left 调用 deleteNode，并返回 root。
如果 root.val<key，表示值为 key 的节点可能存在于 root 的右子树中，需要递归地在 root.right 调用 deleteNode，并返回 root。
如果 root.val=key，root 即为要删除的节点。此时要做的是删除 root，并将它的子树合并成一棵子树，保持有序性，并返回根节点。
根据 root 的子树情况分成以下情况讨论：
    root 为叶子节点，没有子树。此时可以直接将它删除，即返回空。
    root 只有左子树，没有右子树。此时可以将它的左子树作为新的子树，返回它的左子节点。
    root 只有右子树，没有左子树。此时可以将它的右子树作为新的子树，返回它的右子节点。
    root 有左右子树，这时可以将 root 的后继节点（右子树中的最小节点）作为新的根节点替代 root，并将 successor 从 root 的右子树中删除，使得在保持有序性的情况下合并左右子树。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            successor.right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            return successor
        return root
