# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/28 13:29
"""
"""
给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。
返回满足此条件的 任一数组 作为答案。

输入：nums = [3,1,2,4]
输出：[2,4,3,1]
解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。

输入：nums = [0]
输出：[0]
"""
"""
思路：前面找奇数，后面找偶数，交换即可
"""


class Solution(object):
    @staticmethod
    def sortArrayByParity(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            while i<j and nums[i] % 2 == 0:
                i += 1
            while i<j and nums[j] % 2 != 0:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums
