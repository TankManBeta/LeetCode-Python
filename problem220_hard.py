# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/5 12:17
"""
import bisect
from sortedcontainers import SortedList

"""
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，
同时又满足 abs(i - j) <= k 。
如果存在则返回 true，不存在返回 false。

输入：nums = [1,2,3,1], k = 3, t = 0
输出：true

输入：nums = [1,0,1,1], k = 1, t = 2
输出：true

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false
"""
"""
思路：有序链表+滑动窗口，维护一个大小为k的滑动窗口，要是大小超过k，删除最早插入的元素，然后每次看需要插入的数插入的范围以及和左
右两个数之间差值的绝对值是否满足条件即可
"""


class Solution(object):
    @staticmethod
    def containsNearbyAlmostDuplicate(nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        window = SortedList()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= t:
                return True
        return False
