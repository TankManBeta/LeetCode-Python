# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/22 10:36
"""
from functools import cmp_to_key

"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

输入：nums = [10,2]
输出："210"

输入：nums = [3,30,34,5,9]
输出："9534330"
"""
"""
思路：自定义排序顺序，如果int(y+x)-int(x+y)>0，说明后面那个数应该在前面
"""


class Solution(object):
    @staticmethod
    def largestNumber(nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]

        def compare(x, y):
            return int(y+x) - int(x+y)
        nums = sorted(nums, key=cmp_to_key(compare))
        return "0" if nums[0] == "0" else "".join(nums)
