# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/21 14:02
"""
from typing import List

"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回：
[3,9,20,15,7]
"""
"""
思路：bfs即可
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def levelOrder(root: TreeNode) -> List[int]:
        # ans = []
        # if not root:
        #     return ans
        # queue = [root]
        # while queue:
        #     tmp = []
        #     for node in queue:
        #         ans.append(node.val)
        #         if node.left:
        #             tmp.append(node.left)
        #         if node.right:
        #             tmp.append(node.right)
        #     queue = tmp
        # return ans

        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            node = queue.pop(0)
            ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans
