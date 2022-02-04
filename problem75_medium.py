# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/3 15:32
"""
"""
给定一个包含红色、白色和蓝色、共n个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库的sort函数的情况下解决这个问题。

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

输入：nums = [2,0,1]
输出：[0,1,2]
"""
"""
思路：双指针，left换0，right换2，当交换right时，由于不知道交换来的数字是几，所以不能够i++
"""


class Solution(object):
    @staticmethod
    def sort_colors(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while left <= i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                if i <= left:
                    i = left
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
