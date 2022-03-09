# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/8 11:18
"""
from functools import reduce

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

输入: [2,2,1]
输出: 1

输入: [4,1,2,1,2]
输出: 4
"""
"""
思路：
（1）哈希表记录
（2）集合去重后求和sum1，原列表求和sum2，然后因为只出现一次，用2*sum1-sum2
（3）异或操作：任何数和0做异或运算，结果仍然是原来的数；任何数和其自身做异或运算，结果是0
"""


class Solution(object):
    @staticmethod
    def single_number(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res_dict = {}
        # for num in nums:
        #     res_dict[num] = res_dict.get(num, 0) + 1
        # for key, value in res_dict.items():
        #     if value == 1:
        #         return key

        # nums_set = set(nums)
        # sum1 = sum(nums)
        # sum2 = sum(nums_set)
        # return 2*sum2 - sum1

        return reduce(lambda x, y: x ^ y, nums)
