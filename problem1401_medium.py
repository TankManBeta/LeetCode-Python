# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/25 10:18
"""
"""
给你一个以 (radius, xCenter, yCenter) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2) ，其中 (x1, y1) 是矩形左下角的坐标，
而 (x2, y2) 是右上角的坐标。
如果圆和矩形有重叠的部分，请你返回 true ，否则返回 false 。
换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。 

示例 1 ：
输入：radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
输出：true
解释：圆和矩形存在公共点 (1,0) 。

示例 2 ：
输入：radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
输出：false

示例 3 ：
输入：radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
输出：true
"""
"""
思路：只要找到矩形当中离圆心最近的点，然后看a*a+b*b是否小于radius*radius即可。对于x而言，如果圆心的范围在x1~x2之间，说明最短
距离肯定为0，否则的话就是矩形左右端点到圆心距离的最小值；y也同理可得。
"""


class Solution:
    @staticmethod
    def checkOverlap(radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        def f(c, l, r):
            if l <= c <= r:
                return 0
            return min(abs(l-c), abs(r-c))

        a = f(xCenter, x1, x2)
        b = f(yCenter, y1, y2)
        return a*a + b*b <= radius*radius
