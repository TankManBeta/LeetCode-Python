# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/1 9:33
"""
from typing import List

"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。 

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
"""
"""
思路：
（1）直接先排序，然后return前k个即可
（2）基于快排的选择，根据快速排序原理，如果某次哨兵划分后 基准数正好是第 k+1 小的数字 ，那么此时基准数左边的所有数字便是题目
所求的 最小的 k 个数 。
"""


class Solution:
    @staticmethod
    def getLeastNumbers(arr: List[int], k: int) -> List[int]:
        # arr = sorted(arr)
        # return arr[:k]

        if k >= len(arr):
            return arr

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i:
                return quick_sort(l, i - 1)
            if k > i:
                return quick_sort(i + 1, r)
            return arr[:k]

        return quick_sort(0, len(arr) - 1)
