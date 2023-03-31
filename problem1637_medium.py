# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/30 16:11
"""
from math import inf
from typing import List

"""
给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直区域 的宽度。
垂直区域 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直区域 为宽度最大的一个垂直区域。
请注意，垂直区域 边上 的点 不在 区域内。 

示例 1：
输入：points = [[8,7],[9,9],[7,4],[9,7]]
输出：1
解释：红色区域和蓝色区域都是最优区域。

示例 2：
输入：points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
输出：3
"""
"""
思路：
（1）直接排序，然后计算相邻两个数之间的距离，取最大即可。
（2）桶排序。我们将数组 points 的横坐标放入数组 nums 中。假设数组 nums 有 n 个元素，所有元素从小到大依次是 nums0 到 numsn−1 ，
最大间距是 maxGap。考虑数组中的最大元素和最小元素之差：nums[n−1]−nums[0]=≤maxGap×(n−1)。可以利用桶排序的思想，设定桶的大小
（即每个桶最多包含的不同元素个数）为 numsn−1−nums0//n-1，将元素按照元素值均匀分布到各个桶内，则同一个桶内的任意两个元素之差小于 
maxGap，差为 maxGap 的两个元素一定在两个不同的桶内。对于每个桶，维护桶内的最小值和最大值，初始时每个桶内的最小值和最大值分别是
正无穷和负无穷，表示桶内没有元素。
遍历数组 nums 中的所有元素。对于每个元素，根据该元素与最小元素之差以及桶的大小计算该元素应该分到的桶的编号，可以确保编号小的
桶内的元素都小于编号大的桶内的元素，使用元素值更新元素所在的桶内的最小值和最大值。
遍历数组结束之后，每个非空的桶内的最小值和最大值都可以确定。按照桶的编号从小到大的顺序依次遍历每个桶，当前的桶的最小值和上一个
非空的桶的最大值是排序后的相邻元素，计算两个相邻元素之差，并更新最大间距。遍历桶结束之后即可得到最大间距。
"""


class Solution:
    @staticmethod
    def maxWidthOfVerticalArea(points: List[List[int]]) -> int:
        # axis_x = []
        # for x, y in points:
        #     axis_x.append(x)
        # axis_x = sorted(axis_x)
        # n = len(axis_x)
        # ans = 0
        # for i in range(n-1):
        #     ans = max(axis_x[i+1]-axis_x[i], ans)
        # return ans

        nums = [x for x, _ in points]
        n = len(nums)
        mi, mx = min(nums), max(nums)
        bucket_size = max(1, (mx - mi) // (n - 1))
        bucket_count = (mx - mi) // bucket_size + 1
        buckets = [[inf, -inf] for _ in range(bucket_count)]
        for x in nums:
            i = (x - mi) // bucket_size
            buckets[i][0] = min(buckets[i][0], x)
            buckets[i][1] = max(buckets[i][1], x)
        ans = 0
        prev = inf
        for cur_min, cur_max in buckets:
            if cur_min > cur_max:
                continue
            ans = max(ans, cur_min - prev)
            prev = cur_max
        return ans
