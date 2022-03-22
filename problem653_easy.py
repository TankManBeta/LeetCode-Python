# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/21 9:39
"""
"""
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

输入: root = [5,3,6,2,4,null,7], k = 9
输出: true

输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
"""
"""
思路：
（1）dfs+哈希表，判断k-root.val在不在哈希表里
（2）bfs+哈希表，同样判断k-root.val在不在哈希表里
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.s = set()

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        if k - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

        # queue = [root]
        # s = set()
        # while queue:
        #     temp = queue[0]
        #     if k-temp.val in s:
        #         return True
        #     s.add(temp.val)
        #     if temp.left:
        #         queue.append(temp.left)
        #     if temp.right:
        #         queue.append(temp.right)
        #     queue = queue[1:]
        # return False
