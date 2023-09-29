# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/28 22:45
"""
from bisect import bisect_right, bisect_left
from typing import List

"""
给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从 starti 到 endi （都 包含）。
同时给你一个下标从 0 开始大小为 n 的整数数组 people ，people[i] 是第 i 个人来看花的时间。
请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。 

示例 1：
输入：flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
输出：[1,2,2,2]
解释：上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。

示例 2：
输入：flowers = [[1,10],[3,3]], people = [3,3,2]
输出：[2,2,1]
解释：上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。
"""
"""
思路：我们将花按照开始时间和结束时间分别排序，然后对于每个人，我们可以使用二分查找来找到他们到达时在花期内花的数目。就是说，找出在每个人到达时，
已经开花的花的数目，减去在每个人到达时，已经凋谢的花的数目，即可得到答案。
"""


class Solution:
    @staticmethod
    def fullBloomFlowers(flowers: List[List[int]], people: List[int]) -> List[int]:
        start, end = sorted(a for a, _ in flowers), sorted(b for _, b in flowers)
        return [bisect_right(start, p) - bisect_left(end, p) for p in people]
