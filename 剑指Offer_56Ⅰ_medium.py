# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/6 18:07
"""
import functools
from typing import List

"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
"""
"""
思路：首先得到所有数异或的值，然后找到任意一个为1的位，根据这位来对所有的数进行分组，所有相同的数肯定会分到一组并且不同的两个数
肯定会分到不同的组，因为这个1就是不同数的不相同的位置。
"""


class Solution:
    @staticmethod
    def singleNumbers(nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]
