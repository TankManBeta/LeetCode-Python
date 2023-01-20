# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/19 20:42
"""
from math import inf
from typing import List

"""
一个N x N的网格(grid) 代表了一块樱桃地，每个格子由以下三种数字的一种来表示：
    0 表示这个格子是空的，所以你可以穿过它。
    1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
    -1 表示这个格子里有荆棘，挡着你的路。
你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：
    从位置 (0, 0) 出发，最后到达 (N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；
    当到达 (N-1, N-1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
    当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；
    如果在 (0, 0) 和 (N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。

示例 1:
输入: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
输出: 5
解释： 
玩家从（0,0）点出发，经过了向下走，向下走，向右走，向右走，到达了点(2, 2)。
在这趟单程中，总共摘到了4颗樱桃，矩阵变成了[[0,1,-1],[0,0,-1],[0,0,0]]。
接着，这名玩家向左走，向上走，向上走，向左走，返回了起始点，又摘到了1颗樱桃。
在旅程中，总共摘到了5颗樱桃，这是可以摘到的最大值了。
"""
"""
思路：由于从 (N−1,N−1) 返回 (0,0) 的这条路径，可以等价地看成从 (0,0) 到 (N−1,N−1) 的路径，因此问题可以等价转换成，有两个人从 
(0,0) 出发，向下或向右走到 (N−1,N−1) 时，摘到的樱桃个数之和的最大值。
由于题目限制同一个格子只能摘取一次，我们需要找到一种方案来判断两人是否到达了同一个格子。
不妨假设两人同时出发，且速度相同。无论这两人怎么走，在时间相同的情况下，他们向右走的步数加上向下走的步数之和是一个定值（k）。
设两人的坐标为 (x1,y1) 和 (x2,y2)，则x1+y1=x2+y2=k。那么当x1=x2时，必然有 y1=y2，即两个人到达了同一个格子。
定义 f[k][x1][x2] 表示两个人（设为 A 和 B）分别从 (x1,k−x1) 和 (x2,k−x2) 同时出发，到达 (N−1,N−1) 摘到的樱桃个数之和的最大值。
如果 (x1,k−x1) 或 (x2,k−x2) 是荆棘，则 f[k][x1][x2]=−∞，表示不合法的情况。
枚举 A 和 B 上一步的走法，来计算 f[k][x1][x2]。有四种情况：
    都往右：从f[k−1][x1][x2] 转移过来；
    A 往下，B 往右：从 f[k−1][x1−1][x2] 转移过来；
    A 往右，B 往下：从 f[k−1][x1][x2−1] 转移过来；
    都往下：从 f[k−1][x1−1][x2−1] 转移过来；
取这四种情况的最大值，加上 grid[x1][k−x1] 和 grid[x2][k−x2] 的值，就得到了 f[k][x1][x2]，如果 x1=x2，则只需加上 grid[x1][k−x1]。
最后答案为 max(f[2n−2][n−1][n−1],0)，取 max 是因为路径可能被荆棘挡住，无法从 (0,0) 到达 (N−1,N−1)。
"""


class Solution:
    @staticmethod
    def cherryPickup(grid: List[List[int]]) -> int:
        n = len(grid)
        f = [[-inf] * n for _ in range(n)]
        f[0][0] = grid[0][0]
        for k in range(1, n * 2 - 1):
            for x1 in range(min(k, n - 1), max(k - n, -1), -1):
                for x2 in range(min(k, n - 1), x1 - 1, -1):
                    y1, y2 = k - x1, k - x2
                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                        f[x1][x2] = -inf
                        continue
                    res = f[x1][x2]  # 都往右
                    if x1:
                        res = max(res, f[x1 - 1][x2])  # 往下，往右
                    if x2:
                        res = max(res, f[x1][x2 - 1])  # 往右，往下
                    if x1 and x2:
                        res = max(res, f[x1 - 1][x2 - 1])  # 都往下
                    res += grid[x1][y1]
                    if x2 != x1:  # 避免重复摘同一个樱桃
                        res += grid[x2][y2]
                    f[x1][x2] = res
        return max(f[-1][-1], 0)
