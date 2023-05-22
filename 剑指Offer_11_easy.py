# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/20 14:26
"""
from typing import List

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。  
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。 

示例 1：
输入：numbers = [3,4,5,1,2]
输出：1

示例 2：
输入：numbers = [2,2,2,0,1]
输出：0
"""
"""
思路：
（1）直接找数组中的最小值，复杂度为O(n)
（2）二分查找，如果nums[m]<nums[j]，说明旋转点 x 一定在[i,m] 闭区间内，因此执行 j=m；如果nums[m]>nums[j]，说明旋转点在[m+1,j];
当 nums[m]=nums[j] 时： 无法判断 m 在哪个排序数组中，即无法判断旋转点 x 在 [i,m] 还是 [m+1,j] 区间中，执行 j=j−1 缩小判断范围。
"""


class Solution:
    @staticmethod
    def minArray(numbers: List[int]) -> int:
        # return min(numbers)

        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                return min(numbers[i:j])
        return numbers[i]
