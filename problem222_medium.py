# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/5 12:18
"""
"""
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层
最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

输入：root = [1,2,3,4,5,6]
输出：6

输入：root = []
输出：0

输入：root = [1]
输出：1
"""
"""
思路：
（1）dfs或bfs
（2）二分+位运算，充分利用完全二叉树的性质，如果树的深度为h，那么节点的数量肯定在[2^h,2^(h+1)-1]之间，所以我们可以用h+1位表示
路径，为0就说明向左走，为1就说明向右走
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def countNodes(root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def exists(head, level, target):
            bits = 1 << (level - 1)
            node = head
            while node and bits > 0:
                if (bits & target) == 0:
                    node = node.left
                else:
                    node = node.right
                bits >>= 1
            return True if node else False

        if not root:
            return 0

        layer = 0
        temp = root
        while temp.left:
            layer += 1
            temp = temp.left
        low, high = 1 << layer, (1 << (layer + 1)) - 1
        while low < high:
            mid = (high - low + 1) / 2 + low
            if exists(root, layer, mid):
                low = mid
            else:
                high = mid - 1
        return low
