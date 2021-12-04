# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/3 11:06
"""
"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。
例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
"""
"""
思路：头尾指针，如果head的值是val，把tail的值赋过来，tail--；如果head值不为val，head++
"""


class Solution(object):
    @staticmethod
    def remove_element(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        if nums_len == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        i = 0
        j = nums_len-1
        count = 0
        while i <= j:
            if nums[i] != val:
                i += 1
                count += 1
            else:
                if nums[j] == val:
                    j -= 1
                else:
                    nums[i] = nums[j]
                    j -= 1
        return count
