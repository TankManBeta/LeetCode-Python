# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/15 14:53
"""
"""
给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释: 这五个点组成的三角形面积最大为2。
"""
"""
思路：枚举即可
"""


class Solution(object):
    @staticmethod
    def largestTriangleArea(points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        N = len(points)
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(i + 2, N):
                    (x1, y1), (x2, y2), (x3, y3) = points[i], points[j], points[k]
                    res = max(res, 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        return res
