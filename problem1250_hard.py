# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/15 20:31
"""
from functools import reduce
from math import gcd
from typing import List

"""
给你一个正整数数组 nums，你需要从中任选一些子集，然后将子集中每一个数乘以一个 任意整数，并求出他们的和。
假如该和结果为 1，那么原数组就是一个「好数组」，则返回 True；否则请返回 False。

示例 1：
输入：nums = [12,5,7,23]
输出：true
解释：挑选数字 5 和 7。
5*3 + 7*(-2) = 1

示例 2：
输入：nums = [29,6,10]
输出：true
解释：挑选数字 29, 6 和 10。
29*1 + 6*(-3) + 10*(-1) = 1

示例 3：
输入：nums = [3,6]
输出：false
"""
"""
思路：根据裴蜀定理，可以得知，如果 a 和 b 互质，那么上述等式一定有解。实际上，裴蜀定理也可以推广到多个数的情况，即如果 a1,a2,
⋯,ai 互质，那么 a1×x1+a2×x2+⋯+ai×xi=1 一定有解，其中 x1,x2,⋯,xi 是任意整数。因此，我们只需要判断在数组 nums 中是否存在 i 
个互质的数即可。两个数互质的充要条件是它们的最大公约数为 1。如果数组 nums 存在 i 个互质的数，那么数组 nums 中的所有数的最大公
约数也为 1。所以我们将题目转化为：判断数组 nums 中的所有数的最大公约数是否为 1 即可。遍历数组 nums，求出数组 nums 中的所有数
的最大公约数即可。
"""


class Solution:
    @staticmethod
    def isGoodArray(nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1
