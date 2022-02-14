# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/14 20:58
"""
"""
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。
你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

输入: nums =  [3,3,7,7,10,11,11]
输出: 10
"""
"""
思路：
（1）o(n)复杂度：直接每次遍历两个，如果相等就继续下两个，否则就返回两个中的第一个
（2）o(logn)复杂度：二分，如果前面没插入单一的，应该是奇偶这种，否则应该是偶奇这种
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # m = len(nums)
        # for i in range(0, m-1, 2):
        #     if nums[i] != nums[i+1]:
        #         return nums[i]
        # return nums[-1]

        m = len(nums)
        l = 0
        r = m - 1
        while l < r:
            mid = (l + r) / 2
            if mid % 2 == 0:
                if (mid + 1) < m and nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]
