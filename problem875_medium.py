"""
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有piles[i]根香蕉。警卫已经离开了，将在 h 小时后回来。
珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，
然后这一小时内不会再吃更多的香蕉。
珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

输入：piles = [3,6,7,11], h = 8
输出：4

输入：piles = [30,11,23,4,20], h = 5
输出：30

输入：piles = [30,11,23,4,20], h = 6
输出：23
"""
from typing import List

"""
思路：二分查找，最少吃一根，最多吃piles中最多的，然后计算时间，如果时间比h大就说明超时了，左边界右移，否则右边界左移
"""


class Solution:
    @staticmethod
    def min_eating_speed(piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left+right)//2
            total_time = 0
            for i in piles:
                total_time += (i+mid-1)//mid
            if total_time > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
