# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/14 9:58
"""
from typing import List

"""
给定你一个整数数组 nums
我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) == average(B) 。
如果可以完成则返回true ， 否则返回 false  。
注意：对于数组 arr ,  average(arr) 是 arr 的所有元素除以 arr 长度的和。

示例 1:
输入: nums = [1,2,3,4,5,6,7,8]
输出: true
解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。

示例 2:
输入: nums = [3,1]
输出: false
"""
"""
思路：经过推导之后，我们可以得到这样的表达式：sum(A)×n=(sum(nums))×k，也就是说A和B和整个数组的均值是一样的，此时我们可以将数组
nums中的每个元素减去nums的平均值，这样数组nums的平均值则变为0。此时题目中的问题则可以转变为：从nums中找出若干个元素组成集合A，
使得A的元素之和为0，剩下的元素组成集合B，它们的和也同样为0。直接二进制枚举可能会超时，我们考虑将数组分为左右两边，此时情形就分
为三种：第一种左边的有一个子集和为0，第二种右边的有一个子集和为0，第三种左边部分+右边部分的子集和为0。
注：将数组nums中每个元素减去它们的平均值，这一步会引入浮点数，可能会导致判断的时候出现误差。解决方案是先将nums中的每个元素乘以
nums的长度，则此时每个元素nums[i]变为n×nums[i]，这样数组nums的平均值一定为整数，同时也不影响题目中的平均值相等的要求。
需要注意的是，我们不能同时选择A0和B0中的所有元素，这样数组B就为空了。
"""


class Solution:
    @staticmethod
    def splitArraySameAverage(nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        s = sum(nums)
        for i in range(n):
            nums[i] = nums[i] * n - s

        m = n // 2
        left = set()
        for i in range(1, 1 << m):
            tot = sum(x for j, x in enumerate(nums[:m]) if i >> j & 1)
            if tot == 0:
                return True
            left.add(tot)

        rsum = sum(nums[m:])
        for i in range(1, 1 << (n - m)):
            tot = sum(x for j, x in enumerate(nums[m:]) if i >> j & 1)
            if tot == 0 or rsum != tot and -tot in left:
                return True
        return False



