# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/8 9:21
"""
"""
给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。
请你找出所有出现 两次 的整数，并以数组形式返回。
你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。

输入：nums = [4,3,2,7,8,2,3,1]
输出：[2,3]

输入：nums = [1,1,2]
输出：[1]

输入：nums = [1]
输出：[]
"""
"""
思路：
（1）对于当前nums[i]，应该在nums[i]-1的位置上，如果不在的话就一直交换，直到nums[i]在自己的位置上，然后再遍历一遍，
如果当前数和下标不匹配就说明这个位置有没出现过的
（2）对于每一个nums[i]，我们看nums[nums[i]-1]的正负，如果是负的说明出现过，加入ans，否则就把正的变成负的进行标记
"""


class Solution(object):
    @staticmethod
    def findDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     while nums[i] != nums[nums[i] - 1]:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # return [num for i, num in enumerate(nums) if num - 1 != i]

        ans = []
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
            else:
                ans.append(x)
        return ans
