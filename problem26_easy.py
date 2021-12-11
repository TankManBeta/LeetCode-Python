# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/2 20:02
"""
"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
"""
"""
思路：快慢指针，fast找不同的，slow是要填数字的位置。如果相同，fast++；不同就把fast的赋给slow，fast++，slow++。
"""


class Solution(object):
    @staticmethod
    def remove_duplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return nums_len
        fast = 1
        slow = 1
        while fast < nums_len:
            if nums[fast] == nums[fast-1]:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
        return slow
