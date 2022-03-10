# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/9 9:51
"""
"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

输入：nums = [2,2,3,2]
输出：3

输入：nums = [0,1,0,1,0,1,99]
输出：99
"""
"""
思路：
（1）集合去重计算sum1，原数组计算sum2，然后(3sum1-sum2)/2
（2）统计每一位的上出现的1的个数，然后模3.剩下的就是出现一次的
（3）状态转换的推导，推导出逻辑表达式
"""


class Solution(object):
    @staticmethod
    def single_number(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums_set = set(nums)
        # return (3*sum(nums_set) - sum(nums))/2

        # count = [0]*33
        # for x in nums:
        #     if x >= 0:
        #         count[32] += 1
        #     else: x = -x
        #     for i in range(32):
        #         if (x >> i) & 1 == 1:
        #             count[i] += 1
        # ans = 0
        # for i in range(32):
        #     if count[i] % 3 == 1:
        #         ans += 1 << i
        # sign = count[32] % 3
        # return ans if sign == 1 else -ans

        X, Y = 0, 0
        for Z in nums:
            Y = Y ^ Z & ~X
            X = X ^ Z & ~Y
        return Y
