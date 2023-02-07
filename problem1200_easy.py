# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/6 0:35
"""
from typing import List

"""
给你个整数数组 arr，其中每个元素都 不相同。
请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
每对元素对 [a,b] 如下：
    a , b 均为数组 arr 中的元素
    a < b
    b - a 等于 arr 中任意两个元素的最小绝对差
 
示例 1：
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]

示例 2：
输入：arr = [1,3,6,10,15]
输出：[[1,3]]

示例 3：
输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]
"""
"""
思路：首先我们对数组 arr 进行升序排序。这样一来，拥有「最小绝对差」的元素对只能由有序数组中相邻的两个元素构成。随后我们对数组 
arr 进行一次遍历。当遍历到 arr[i] 和 arr[i+1] 时，它们的差为 δ=arr[i+1]−arr[i]。我们使用一个变量 best 存储当前遇到的最小差，
以及一个数组 ans 存储答案：
如果 δ<best，那么说明我们遇到了更小的差值，需要更新 best，同时 ans 清空并放入 arr[i] 和 arr[i+1]；
如果 δ=best，那么我们只需要将 arr[i] 和 arr[i+1] 放入答案数组即可。
"""


class Solution:
    @staticmethod
    def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_gap = 10 ** 7
        res = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] < min_gap:
                min_gap = arr[i + 1] - arr[i]
                res = [[arr[i], arr[i + 1]]]
            elif arr[i + 1] - arr[i] == min_gap:
                res.append([arr[i], arr[i + 1]])
        return res
