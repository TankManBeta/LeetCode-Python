# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/20 11:36
"""
"""
给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树。

输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。

输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
"""
"""
思路：
（1）带pre指针的中序遍历，o(n)复杂度
（2）Morris遍历，左子树的最右子树的next指向root，o(1)复杂度
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def recover_tree(root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # self.x = None
        # self.y = None
        # self.pre = None
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     if not self.pre:
        #         self.pre = root
        #     else:
        #         if self.pre.val>root.val:
        #             self.y = root
        #             if not self.x:
        #                 self.x = self.pre
        #         self.pre = root
        #     dfs(root.right)
        # dfs(root)

        # if self.x and self.y:
        #     self.x.val,self.y.val = self.y.val,self.x.val
        x = None
        y = None
        pre = None
        tmp = None
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if tmp.right is None:
                    tmp.right = root
                    root = root.left
                else:
                    if pre and pre.val>root.val:
                        y = root
                        if not x:
                            x = pre
                    pre = root
                    tmp.right = None
                    root = root.right
            else:
                if pre and pre.val>root.val:
                    y = root
                    if not x:
                        x = pre
                pre = root
                root = root.right
        if x and y:
            x.val, y.val = y.val, x.val
