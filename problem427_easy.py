# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/30 12:58
"""
"""
给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。
你需要返回能表示矩阵的 四叉树 的根结点。
注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。
四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：
val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。

输入：grid = [[0,1],[1,0]]
输出：[[0,1],[1,0],[1,1],[1,1],[1,0]]

输入：grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
输出：[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]

输入：grid = [[1,1],[1,1]]
输出：[[1,1]]

输入：grid = [[0]]
输出：[[1,0]]

输入：grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
输出：[[0,1],[1,1],[1,0],[1,0],[1,1]]
"""
"""
思路：简单建树题，用递归，如果当前正方形全是一个数，则是叶子节点，否则不是，用前缀和看是否全是一个数
"""


# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    @staticmethod
    def construct(grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        pre = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + grid[i - 1][j - 1]

        def getSum(r0, c0, r1, c1):
            return pre[r1][c1] - pre[r1][c0] - pre[r0][c1] + pre[r0][c0]

        def dfs(r0, c0, r1, c1):
            total = getSum(r0, c0, r1, c1)
            if total == 0:
                return Node(False, True)
            if total == (r1 - r0) * (c1 - c0):
                return Node(True, True)
            return Node(
                True,
                False,
                dfs(r0, c0, (r0 + r1) // 2, (c0 + c1) // 2),
                dfs(r0, (c0 + c1) // 2, (r0 + r1) // 2, c1),
                dfs((r0 + r1) // 2, c0, r1, (c0 + c1) // 2),
                dfs((r0 + r1) // 2, (c0 + c1) // 2, r1, c1),
            )

        return dfs(0, 0, n, n)
