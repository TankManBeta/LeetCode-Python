# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/9 19:34
"""
"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

输入：nums = [1,2,0]
输出：3

输入：nums = [3,4,-1,1]
输出：2

输入：nums = [7,8,9,11,12]
输出：1
"""
"""
思路：
（1）直接hash，将键值存进字典，然后再取key，取不到就是所求答案，但不满足空间复杂度
（2）看完题解，从前往后遍历，如果0<nums[i]<=len(nums)，就把它换到对应的nums[nums[i]-1]的位置上，然后从头遍历，num[j]!=j+1的
就是缺整数的位置，遍历完都不差的话就返回length+1
"""


# 不满足空间复杂度
# class Solution(object):
#     def firstMissingPositive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res_dict = {}
#         for num in nums:
#             if num <= 0:
#                 continue
#             else:
#                 res_dict[num] = num
#
#         for i in range(1, len(nums) + 1):
#             if res_dict.get(i, -1) == -1:
#                 return i
#         return len(nums) + 1


class Solution(object):
    @staticmethod
    def first_missing_positive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        nums_len = len(nums)
        while i < len(nums):
            if 0 < nums[i] <= nums_len and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
            else:
                i += 1
        for j in range(0, nums_len):
            if nums[j] != j + 1:
                return j+1
        return nums_len + 1
