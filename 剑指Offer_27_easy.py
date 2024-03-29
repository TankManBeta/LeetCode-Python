# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/22 10:33
"""
"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
例如输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""
"""
思路：递归改变左右子树即可
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # def dfs(head):
        #     if not head:
        #         return
        #     head.left, head.right = head.right, head.left
        #     self.mirrorTree(head.left)
        #     self.mirrorTree(head.right)

        # dfs(root)
        # return root

        if not root:
            return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root
