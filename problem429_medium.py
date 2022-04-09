# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/8 9:53
"""
"""
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

输入：root = [1,null,3,2,4,null,5,6]
输出：[[1],[3,2,4],[5,6]]

输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
"""
"""
思路：简单bfs即可
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    @staticmethod
    def levelOrder(root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            queue_len = len(queue)
            temp_ans = []
            for i in range(queue_len):
                temp_node = queue.pop(0)
                temp_ans.append(temp_node.val)
                for node in temp_node.children:
                    queue.append(node)
            ans.append(temp_ans)
        return ans
