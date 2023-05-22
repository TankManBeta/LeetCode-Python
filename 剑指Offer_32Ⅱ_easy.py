# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/21 14:12
"""
from typing import List

"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
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
    def levelOrder(root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            tmp = []
            tmp_ans = []
            for node in queue:
                tmp_ans.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            ans.append(tmp_ans)
        return ans
