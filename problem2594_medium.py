# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/7 22:09
"""
from bisect import bisect_left
from math import sqrt
from typing import List

"""
给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。
同时给你一个整数 cars ，表示总共需要修理的汽车数目。
请你返回修理所有汽车 最少 需要多少时间。
注意：所有机械工可以同时修理汽车。 

示例 1：
输入：ranks = [4,2,3,1], cars = 10
输出：16
解释：
- 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
- 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
- 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
- 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
16 分钟是修理完所有车需要的最少时间。

示例 2：
输入：ranks = [5,1,8], cars = 6
输出：16
解释：
- 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
- 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
- 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
16 分钟时修理完所有车需要的最少时间。
"""
"""
思路：我们定义二分查找的左右边界分别为 left=0, right=ranks[0]×cars×cars。接下来二分枚举修车时间 mid，每个机械工可以修理的汽车数目为 
⌊根号mid/r⌋，其中 ⌊x⌋ 表示向下取整。如果修理的汽车数目大于等于 cars，则说明修车时间 mid 可行，我们将右边界缩小至 mid，否则将左边界增大至 
mid+1。最终，我们返回左边界即可。
"""


class Solution:
    @staticmethod
    def repairCars(ranks: List[int], cars: int) -> int:
        def check(t: int) -> bool:
            return sum(int(sqrt(t // r)) for r in ranks) >= cars

        return bisect_left(range(ranks[0] * cars * cars), True, key=check)
