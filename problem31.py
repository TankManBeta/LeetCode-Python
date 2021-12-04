# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/4 18:22
"""
"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。

输入：nums = [1,2,3]
输出：[1,3,2]

输入：nums = [3,2,1]
输出：[1,2,3]

输入：nums = [1,1,5]
输出：[1,5,1]

输入：nums = [1]
输出：[1]
"""
"""
思路：
先从后往前找一个nums[i-1]<nums[i]的，说明i-1是要交换的位置；
如果找不到说明已经是最大的了，直接倒排整个数组；
从后往前找第一个比i-1位置上大的数字，交换两个数字；
i到最后倒排即可。

[1,2,7,4,3,1] -> 2<7，找到2 -> 3>1，找到3 -> 交换2和3 -> 倒排7到最后
"""


class Solution(object):
    @staticmethod
    def next_permutation(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 定义一个将nums中[i,j]区间的元素原地倒排的函数
        def reverse(nums_list, start, end):
            while start < end:
                nums_list[start], nums_list[end] = nums_list[end], nums_list[start]
                start += 1
                end -= 1

        len_nums = len(nums)
        first_index = -1
        for i in range(len_nums-1, 0, -1):
            if nums[i] > nums[i - 1]:
                # 需要交换的下标
                first_index = i-1
                break

        # 返回-1说明已经是最大的，直接全部倒排
        if first_index == -1:
            reverse(nums, 0, len_nums-1)
            return

        # 从右至左找第一个大于nums[firstIndex]的大数
        second_index = -1
        for i in range(len_nums-1, first_index, -1):
            if nums[i] > nums[first_index]:
                second_index = i
                break

        # 交换两个index的值
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]

        # 将第一个index后面的全都升序排列
        reverse(nums, first_index+1, len_nums-1)
