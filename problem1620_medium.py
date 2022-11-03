# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/2 11:03
"""
from typing import List

"""
给你一个数组 towers 和一个整数 radius 。
数组  towers  中包含一些网络信号塔，其中 towers[i] = [xi, yi, qi] 表示第 i 个网络信号塔的坐标是 (xi, yi) 且信号强度参数为 qi 。
所有坐标都是在  X-Y 坐标系内的 整数 坐标。两个坐标之间的距离用 欧几里得距离 计算。
整数 radius 表示一个塔 能到达 的 最远距离 。如果一个坐标跟塔的距离在 radius 以内，那么该塔的信号可以到达该坐标。
在这个范围以外信号会很微弱，所以 radius 以外的距离该塔是 不能到达的 。
如果第 i 个塔能到达 (x, y) ，那么该塔在此处的信号为 ⌊qi / (1 + d)⌋ ，其中 d 是塔跟此坐标的距离。
一个坐标的 信号强度 是所有 能到达 该坐标的塔的信号强度之和。
请你返回数组 [cx, cy] ，表示 信号强度 最大的 整数 坐标点 (cx, cy) 。如果有多个坐标网络信号一样大，请你返回字典序最小的非负坐标。
注意：
坐标 (x1, y1) 字典序比另一个坐标 (x2, y2) 小，需满足以下条件之一：
    要么 x1 < x2 ，
    要么 x1 == x2 且 y1 < y2 。
⌊val⌋ 表示小于等于 val 的最大整数（向下取整函数）。

示例 1：
输入：towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
输出：[2,1]
解释：
坐标 (2, 1) 信号强度之和为 13
- 塔 (2, 1) 强度参数为 7 ，在该点强度为 ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
- 塔 (1, 2) 强度参数为 5 ，在该点强度为 ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
- 塔 (3, 1) 强度参数为 9 ，在该点强度为 ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
没有别的坐标有更大的信号强度。

示例 2：
输入：towers = [[23,11,21]], radius = 9
输出：[23,11]
解释：由于仅存在一座信号塔，所以塔的位置信号强度最大。

示例 3：
输入：towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
输出：[1,2]
解释：坐标 (1, 2) 的信号强度最大。
"""
"""
思路：直接暴力，首先确定能搜索的最大范围，然后对于范围里的每一点，计算到tower的距离，合法范围内就quality+=计算出来的值，然后比较
max_quality和当前quality的值，当前quality大的话就更新，因为是从小到大计算，所以不需要考虑字典序的问题。
"""


class Solution:
    @staticmethod
    def bestCoordinate(towers: List[List[int]], radius: int) -> List[int]:
        min_x = max(0, min([tower[0] for tower in towers])-radius)
        min_y = max(0, min([tower[1] for tower in towers])-radius)
        max_x = max([tower[0] for tower in towers]) + radius
        max_y = max([tower[1] for tower in towers]) + radius
        res_x, res_y, res_quality = 0, 0, 0
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                quality = 0
                for tx, ty, q in towers:
                    d = (i - tx) ** 2 + (j - ty) ** 2
                    if d <= radius ** 2:
                        quality += int(q / (1 + d ** 0.5))
                    if quality > res_quality:
                        res_x, res_y, res_quality = i, j, quality
        return [res_x, res_y]
