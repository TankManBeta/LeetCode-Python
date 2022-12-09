# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/8 10:43
"""
"""
给你一个坐标 coordinates ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。下图是国际象棋棋盘示意图。
如果所给格子的颜色是白色，请你返回 true，如果是黑色，请返回 false 。
给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。

示例 1：
输入：coordinates = "a1"
输出：false
解释：如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false 。

示例 2：
输入：coordinates = "h3"
输出：true
解释：如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true 。

示例 3：
输入：coordinates = "c7"
输出：false
"""
"""
思路：简单题，找规律即可
"""


class Solution:
    @staticmethod
    def squareIsWhite(coordinates: str) -> bool:
        mapping1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        mapping2 = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}
        m = mapping1[coordinates[0]]
        n = mapping2[coordinates[1]]
        return (m % 2 == 0 and n % 2 != 0) or (m % 2 != 0 and n % 2 == 0)
