# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/13 9:55
"""
"""
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

输入: nums = [2,3,0,1,4]
输出: 2
"""
"""
思路：从头开始，每次计算当前位置可以到达的最远距离，到达边界就更新边界为最大距离，step++，最后返回step
"""


class Solution(object):
    @staticmethod
    def jump(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        end, max_pos, steps = 0, 0, 0
        for i in range(0, nums_len-1):
            max_pos = max(max_pos, nums[i]+i)
            if i == end:
                end = max_pos
                steps += 1
        return steps
