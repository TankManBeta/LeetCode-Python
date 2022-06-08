"""
给定一个数组points，其中points[i] = [xi, yi]表示 X-Y 平面上的一个点，如果这些点构成一个回旋镖则返回true。
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。

输入：points = [[1,1],[2,3],[3,2]]
输出：true

输入：points = [[1,1],[2,2],[3,3]]
输出：false
"""
from typing import List

"""
思路：判断三点不共线，即判断叉乘是否为0
"""


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        v2 = (points[2][0] - points[0][0], points[2][1] - points[0][1])
        return v1[0] * v2[1] - v1[1] * v2[0] != 0
