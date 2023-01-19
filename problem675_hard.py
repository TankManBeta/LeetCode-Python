# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/18 19:10
"""
from collections import deque
from typing import List

"""
你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：
    0 表示障碍，无法触碰
    1 表示地面，可以行走
    比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。
你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。
你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。
可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

示例 1：
输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。

示例 2：
输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。

示例 3：
输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。
"""
"""
思路：首先对矩阵中的树按照树的高度进行排序，我们依次求出相邻的树之间的最短距离。利用广度优先搜索，按照层次遍历，处理队列中的节点
（网格位置）。visited 记录在某个时间点已经添加到队列中的节点，这些节点已被处理或在等待处理的队列中。对于下一个要处理的每个节点，
查看他们的四个方向上相邻的点，如果相邻的点没有被遍历过且不是障碍，将其加入到队列中，直到找到终点为止，返回当前的步数即可。最终
返回所有的步数之和即为最终结果。
"""


class Solution:
    @staticmethod
    def cutOffTree(forest: List[List[int]]) -> int:
        def bfs(sx: int, sy: int, tx: int, ty: int) -> int:
            m, n = len(forest), len(forest[0])
            q = deque([(0, sx, sy)])
            vis = {(sx, sy)}
            while q:
                dis, x, y = q.popleft()
                if x == tx and y == ty:
                    return dis
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < m and 0 <= ny < n and forest[nx][ny] and (nx, ny) not in vis:
                        vis.add((nx, ny))
                        q.append((dis + 1, nx, ny))
            return -1

        trees = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
        ans = preI = preJ = 0
        for _, i, j in trees:
            d = bfs(preI, preJ, i, j)
            if d < 0:
                return -1
            ans += d
            preI, preJ = i, j
        return ans
