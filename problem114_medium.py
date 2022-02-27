# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/26 13:16
"""
"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

输入：root = []
输出：[]

输入：root = [0]
输出：[0]
"""
"""
思路：
（1）直接先序遍历存节点，然后再依次连起来
（2）找到当前结点右子树的前驱节点，即当前节点左子树的最右节点，然后把当前节点右子树挂到前驱节点的右子树，当前节点的左子树挂到
右子树，左子树指向空即可
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def flatten(root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # pre_list = list()

        # def pre_traversal(root):
        #     if root:
        #         pre_list.append(root)
        #         pre_traversal(root.left)
        #         pre_traversal(root.right)

        # pre_traversal(root)
        # size = len(pre_list)
        # for i in range(1, size):
        #     prev, curr = pre_list[i - 1], pre_list[i]
        #     prev.left = None
        #     prev.right = curr

        cur = root
        while cur:
            if cur.left:
                prev = next = cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur.right
                cur.right = next
                cur.left = None
            cur = cur.right
