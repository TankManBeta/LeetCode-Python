# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/29 15:50
"""
from typing import List

"""
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下
种入 n 朵花？能则返回 true ，不能则返回 false 。 

示例 1：
输入：flowerbed = [1,0,0,0,1], n = 1
输出：true

示例 2：
输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
"""
"""
思路：我们直接遍历数组 flowerbed，对于每个位置 i，如果 flowerbed[i]=0，并且其左右相邻位置都为 0，则我们可以在该位置种花，否则不能。最后
我们统计可以种下的花的数量，如果其不小于 n，则返回 true，否则返回 false。
"""


class Solution:
    @staticmethod
    def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if sum(flowerbed[i - 1: i + 2]) == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
