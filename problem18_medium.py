# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/1 15:10
"""
"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] 
（若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
"""
"""
思路：
同三数之和，先用二层循环确定前两个数字，再加上剩下两个数字求和。
"""


class Solution(object):
    @staticmethod
    def four_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        nums_len = len(nums)
        if nums_len < 4:
            return []
        res_list = []
        for i in range(0, nums_len-3):
            for j in range(i+1, nums_len-2):
                start = j+1
                end = nums_len-1
                while start < end:
                    temp_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[start] + sorted_nums[end]
                    if temp_sum == target:
                        opt = [sorted_nums[i], sorted_nums[j], sorted_nums[start], sorted_nums[end]]
                        if opt not in res_list:
                            res_list.append(opt)
                        start += 1
                        end -= 1
                    elif temp_sum < target:
                        start += 1
                    else:
                        end -= 1
        return res_list