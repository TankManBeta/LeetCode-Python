# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/16 11:08
"""
"""
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
如果指定节点没有对应的“下一个”节点，则返回null。

输入: root = [2,1,3], p = 1
输出: 2

输入: root = [5,3,6,2,4,null,null,1], p = 6
输出: null
"""
"""
思路：根据BST的性质，如果root.val<=p.val，说明后继在root的右子树上；如果root.val>p.val说明在左子树上，如果左子树空的话说明就是
结果就是root，否则的话就是左子树上找到的
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        ans = self.inorderSuccessor(root.left, p)
        return root if not ans else ans
