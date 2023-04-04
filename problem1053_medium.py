# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/3 10:36
"""
from typing import List

"""
给你一个正整数数组 arr（可能存在重复的元素），请你返回可在 一次交换（交换两数字 arr[i] 和 arr[j] 的位置）后得到的、
按字典序排列小于 arr 的最大排列。
如果无法这么操作，就请返回原数组。

示例 1：
输入：arr = [3,2,1]
输出：[3,1,2]
解释：交换 2 和 1

示例 2：
输入：arr = [1,1,5]
输出：[1,1,5]
解释：已经是最小排列

示例 3：
输入：arr = [1,9,4,6,7]
输出：[1,7,4,6,9]
解释：交换 9 和 7
"""
"""
思路：贪心。要想交换后小于原arr，且无限接近原arr，必须使交换位置尽量靠右，以此确定从右往左的查找方向；找i，从右向左，找第一个
arr[i-1] > arr[i]的下标i-1，因为只有这样把arr[i-1]换到更后面，才能使字典序变小；确定i-1后，可以发现，i-1下标右侧是一个升序数组，
其中(可能)有比arr[i-1]大的，也(可能)有比arr[i-1]小的；找j，从右往左，找第一个arr[j] < arr[i-1]的，如果有连续多个arr[j]，
找最左端那个，符合无限接近的要求。
"""


class Solution:
    @staticmethod
    def prevPermOpt1(arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                for j in range(n - 1, i - 1, -1):
                    if arr[j] < arr[i - 1] and arr[j] != arr[j - 1]:
                        arr[i - 1], arr[j] = arr[j], arr[i - 1]
                        return arr
        return arr
