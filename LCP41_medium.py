# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/21 22:59
"""
from collections import deque
from typing import List

"""
在 n*m 大小的棋盘中，有黑白两种棋子，黑棋记作字母 "X", 白棋记作字母 "O"，空余位置记作 "."。当落下的棋子与其他相同颜色的棋子在行、
列或对角线完全包围（中间不存在空白位置）另一种颜色的棋子，则可以翻转这些棋子的颜色。
「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 chessboard。若下一步可放置一枚黑棋，
请问选手最多能翻转多少枚白棋。

注意：
若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 继续 翻转白棋
输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置

示例 1：
输入：chessboard = ["....X.","....X.","XOOO..","......","......"]
输出：3
解释：可以选择下在 [2,4] 处，能够翻转白方三枚棋子。

示例 2：
输入：chessboard = [".X.",".O.","XO."]
输出：2
解释：可以选择下在 [2,2] 处，能够翻转白方两枚棋子。

示例 3：
输入：chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]
输出：4
解释：可以选择下在 [6,3] 处，能够翻转白方四枚棋子。
"""
"""
思路：BFS，我们注意到，题目中棋盘的大小最大为 8×8，因此，我们可以尝试枚举所有的空余位置作为下一步放置黑棋的位置，然后使用广度
优先搜索的方法计算在该位置下可以翻转的白棋的数量，找出最大值即可。我们定义一个函数 bfs(i,j)，表示在棋盘上放置黑棋在 (i,j) 位置后，
可以翻转的白棋的数量。在函数中，我们使用队列来进行广度优先搜索，初始时将 (i,j) 放入队列中，然后不断取出队首位置，遍历棋盘的八个
方向，如果该方向上是一段连续的白棋，且在末尾是黑棋，则将该黑棋之前的所有白棋都可以翻转，将这些白棋的位置放入队列中，继续进行广度
优先搜索。最后，我们返回可以翻转的白棋的数量。
"""


class Solution:
    @staticmethod
    def flipChess(chessboard: List[str]) -> int:
        def bfs(i: int, j: int) -> int:
            q = deque([(i, j)])
            g = [list(row) for row in chessboard]
            g[i][j] = 'X'
            cnt = 0
            while q:
                i, j = q.popleft()
                for a, b in dirs:
                    x, y = i + a, j + b
                    while 0 <= x < m and 0 <= y < n and g[x][y] == 'O':
                        x, y = x + a, y + b
                    if 0 <= x < m and 0 <= y < n and g[x][y] == 'X':
                        x, y = x - a, y - b
                        cnt += max(abs(x - i), abs(y - j))
                        while x != i or y != j:
                            g[x][y] = 'X'
                            q.append((x, y))
                            x, y = x - a, y - b
            return cnt

        m, n = len(chessboard), len(chessboard[0])
        dirs = [(a, b) for a in range(-1, 2) for b in range(-1, 2) if a != 0 or b != 0]
        return max(bfs(i, j) for i in range(m) for j in range(n) if chessboard[i][j] == '.')
