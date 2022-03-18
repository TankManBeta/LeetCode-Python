# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/17 11:03
"""
"""
已知一个长度为 n 的数组，预先按照升序排列，经由1到n次旋转后，得到输入数组。例如，原数组nums=[0,1,4,4,5,6,7]在变化后可能得到：
    若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
    若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
你必须尽可能减少整个过程的操作步骤。

输入：nums = [1,3,5]
输出：1

输入：nums = [2,2,2,0,1]
输出：0
"""
"""
思路：二分即可，右边大于中间，就把右边界缩小到mid；如果右边小于中间，就把左边界放缩到mid+1；如果相等就把右边界减一
"""


class Solution(object):
    @staticmethod
    def find_min(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]