# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/12 10:45
"""
"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

输入：nums = [1,2,1,3,2,5]
输出：[3,5]
解释：[5, 3] 也是有效的答案。

输入：nums = [-1,0]
输出：[-1,0]

输入：nums = [0,1]
输出：[1,0]
"""
"""
思路：
（1）直接遍历，如果num已经出现过就删掉，否则放进ans
（2）先将所有数字异或起来得到的结果是x1和x2的异或，取最后一位1就能得到x1和x2第一个不同的位置，然后通过这个位置将数字分为两类：
对于任意一个在数组nums中出现两次的元素，该元素的两次出现会被包含在同一类中；对于任意一个在数组nums中只出现了一次的元素，即x1和
x2，它们会被包含在不同类中。
"""


class Solution(object):
    @staticmethod
    def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ans = []
        # for num in nums:
        #     if num in ans:
        #         ans.remove(num)
        #     else:
        #         ans.append(num)
        # return ans

        x_or_sum = 0
        for num in nums:
            x_or_sum ^= num

        lsb = x_or_sum & (-x_or_sum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num

        return [type1, type2]
