# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/21 14:33
"""
from typing import List

"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
  [20,9],
  [15,7]
]
"""
"""
思路：bfs，设置一个标志位即可
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
        if not root:
            return []
        ans = []
        queue = [root]
        flag = 0
        while queue:
            tmp_ans = []
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp_ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flag:
                ans.append(tmp_ans[::-1])
                flag = 0
            else:
                ans.append(tmp_ans)
                flag = 1
        return ans
