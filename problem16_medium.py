# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/1 14:00
"""
"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

输入：nums = [0,0,0], target = 1
输出：0
"""
"""
思路：
同上一题，排序之后头尾指针
"""


class Solution:
    @staticmethod
    def three_sum_closest(nums, target):
        num_len = len(nums)
        sorted_nums = sorted(nums)
        closest_sum = 100000
        relative_gap = 100000
        for i in range(0, num_len-2):
            start = i+1
            end = num_len-1
            while start < end:
                temp_sum = sorted_nums[i] + sorted_nums[start] + sorted_nums[end]
                if temp_sum == target:
                    closest_sum = target
                    return closest_sum
                elif temp_sum < target:
                    if abs(target-temp_sum) < relative_gap:
                        relative_gap = abs(target - temp_sum)
                        closest_sum = temp_sum
                    start += 1
                else:
                    if abs(target - temp_sum) < relative_gap:
                        relative_gap = abs(target - temp_sum)
                        closest_sum = temp_sum
                    end -= 1
        return closest_sum
