# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/6 20:46
"""
from typing import List

"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。 

示例 1：
输入：nums = [3,4,3,3]
输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1
"""
"""
思路：有限状态机，只需要看每一个二进制位上的1的个数对3取模，就能知道只出现一次的那个数当前二进制位是0还是1。因为有三种情况，所以
需要两个二进制位表示这三种情况，变化的规律是00->01->10->00...，状态机的转移方程：ones = ones ^ num & ~twos；twos = twos ^ num & ~ones
"""


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
