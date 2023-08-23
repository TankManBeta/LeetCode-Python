# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/23 0:06
"""
from typing import List

"""
给你一个数组 seats 表示一排座位，其中 seats[i] = 1 代表有人坐在第 i 个座位上，seats[i] = 0 代表座位 i 上是空的（下标从 0 开始）。
至少有一个空座位，且至少有一人已经坐在座位上。
亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
返回他到离他最近的人的最大距离。 

示例 1：
输入：seats = [1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。 

示例 2：
输入：seats = [1,0,0,0]
输出：3
解释：
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。

示例 3：
输入：seats = [0,1]
输出：1
"""
"""
思路：我们定义两个变量 first 和 last 分别表示第一个人和最后一个人的位置，用变量 d 表示两个人之间的最大距离。然后遍历数组 seats，
如果当前位置有人，如果此前 last 更新过，说明此前有人，此时更新 d=max(d,i−last)；如果此前 first 没有更新过，说明此前没有人，
此时更新 first=i。接下来更新 last=i。最后返回 max(first,n−last−1,d/2) 即可。
"""


class Solution:
    @staticmethod
    def maxDistToClosest(seats: List[int]) -> int:
        first = last = None
        d = 0
        for i, c in enumerate(seats):
            if c:
                if last is not None:
                    d = max(d, i - last)
                if first is None:
                    first = i
                last = i
        return max(first, len(seats) - last - 1, d // 2)
