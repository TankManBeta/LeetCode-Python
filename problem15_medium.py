# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/30 22:07
"""
"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

输入：nums = []
输出：[]

输入：nums = [0]
输出：[]
"""
"""
思路：
一开始思路被限制在了两数之和的问题上，后来想可以用双指针，先升序排数组，然后从第一个开始，用头尾双指针，找两个数的和为想要的。
如果值大了就把尾部索引减1，值小了就把头部索引加1。
"""


class Solution(object):
    @staticmethod
    def three_sum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        increasing_list = sorted(nums)
        list_len = len(nums)
        res_list = []
        for i in range(0, list_len):
            number1 = increasing_list[i]
            if number1 > 0:
                return res_list
            remainder = -increasing_list[i]
            start = i+1
            end = list_len-1
            while start < end:
                if increasing_list[start] + increasing_list[end] == remainder:
                    option = [number1, increasing_list[start], increasing_list[end]]
                    if option not in res_list:
                        res_list.append(option)
                    start += 1
                    end -= 1
                elif increasing_list[start] + increasing_list[end] < remainder:
                    start += 1
                else:
                    end -= 1
        return res_list
