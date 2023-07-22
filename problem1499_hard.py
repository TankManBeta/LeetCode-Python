# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/21 9:10
"""
from cmath import inf
from collections import deque
from typing import List

"""
给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。也就是说 
points[i] = [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。
请你找出 yi + yj + |xi - xj| 的 最大值，其中 |xi - xj| <= k 且 1 <= i < j <= points.length。
题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。

示例 1：
输入：points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
输出：4
解释：前两个点满足 |xi - xj| <= 1 ，代入方程计算，则得到值 3 + 0 + |1 - 2| = 4 。第三个和第四个点也满足条件，得到值 10 + -10 + |5 - 6| = 1 。
没有其他满足条件的点，所以返回 4 和 1 中最大的那个。

示例 2：
输入：points = [[0,0],[3,0],[9,2]], k = 3
输出：3
解释：只有前两个点满足 |xi - xj| <= 3 ，代入方程后得到值 0 + 0 + |0 - 3| = 3 。
"""
"""
思路：变形：yi+yj+∣xi−xj∣=yi+yj+xj−xi=(yi−xi)+(xj+yj)​。枚举j，问题变成计算 yi−xi 的最大值，其中 i<j 且 xi≥xj−k 。
用单调队列优化：单调队列存储二元组 (xi,yi−xi)。首先把队首的超出范围的数据出队，即 xi<xj−k 的数据。然后把(xj,yj−xj) 入队，
入队前如果发现 yj−xj 不低于队尾的数据，那么直接弹出队尾。这样维护后，单调队列的 yi−xi 从队首到队尾是严格递减的，yi−xi的最大值
即为队首的最大值。
"""


class Solution:
    @staticmethod
    def findMaxValueOfEquation(points: List[List[int]], k: int) -> int:
        ans = -inf
        q = deque()
        for x, y in points:
            while q and q[0][0] < x - k:
                q.popleft()
            if q:
                ans = max(ans, x + y + q[0][1])
            while q and q[-1][1] <= y - x:
                q.pop()
            q.append((x, y - x))
        return ans
