# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/17 11:26
"""
"""
峰值元素是指其值严格大于左右相邻值的元素。
给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设 nums[-1] = nums[n] = -∞ 。
你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；或者返回索引 5， 其峰值元素为 6。
"""
"""
思路：采用类似二分的思路，如果中间的是峰顶，直接返回；如果中间不是峰顶且比mid+1小，就往右走，因为mid+1及其右边一定右一个峰顶；
否则向左走
"""


class Solution(object):
    @staticmethod
    def find_peak_element(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def get(index):
            if index == -1 or index == n:
                return float('-inf')
            return nums[index]

        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return ans
