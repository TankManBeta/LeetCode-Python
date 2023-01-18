# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/17 17:19
"""
from typing import List, Tuple

"""
给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。
点的坐标 pi 表示为 [xi, yi] 。 输入没有任何顺序 。
一个 有效的正方形 有四条等边和四个等角(90度角)。

示例 1:
输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True

示例 2:
输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
输出：false

示例 3:
输入：p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
输出：true
"""
"""
思路：判别正方形的一般顺序为先说明它是平行四边形；再说明它是菱形（或矩形）；最后说明它是矩形（或菱形）。如果两条斜边的中点相同：
则说明以该两条斜边组成的四边形为「平行四边形」。在满足「条件一」的基础上，如果两条斜边的长度相同：则说明以该两条斜边组成的四边形
为「矩形」。在满足「条件二」的基础上，如果两条斜边的相互垂直：则说明以该两条斜边组成的四边形为「正方形」。
"""


def checkLength(v1: Tuple[int, int], v2: Tuple[int, int]) -> bool:
    return v1[0] * v1[0] + v1[1] * v1[1] == v2[0] * v2[0] + v2[1] * v2[1]


def checkMidPoint(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    return p1[0] + p2[0] == p3[0] + p4[0] and p1[1] + p2[1] == p3[1] + p4[1]


def calCos(v1: Tuple[int, int], v2: Tuple[int, int]) -> int:
    return v1[0] * v2[0] + v1[1] * v2[1]


def my_help(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    v1 = (p1[0] - p2[0], p1[1] - p2[1])
    v2 = (p3[0] - p4[0], p3[1] - p4[1])
    return checkMidPoint(p1, p2, p3, p4) and checkLength(v1, v2) and calCos(v1, v2) == 0


class Solution:
    @staticmethod
    def validSquare(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2:
            return False
        if my_help(p1, p2, p3, p4):
            return True
        if p1 == p3:
            return False
        if my_help(p1, p3, p2, p4):
            return True
        if p1 == p4:
            return False
        if my_help(p1, p4, p2, p3):
            return True
        return False
