# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/4 11:16
"""
"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""
"""
思路：用哈希表，如果当前数字不在哈希表中，找它左右相邻两个数的长度，然后更新cur_length，然后在更新左右两端能到达的最远位置的
长度，因为已经连通了
"""


class Solution(object):
    @staticmethod
    def longest_consecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        res_dict = {}
        for num in nums:
            if num not in res_dict:
                left_length = res_dict.get(num-1, 0)
                right_length = res_dict.get(num+1, 0)
                cur_length = left_length+right_length+1
                if cur_length > max_length:
                    max_length = cur_length
                res_dict[num] = cur_length
                res_dict[num-left_length] = cur_length
                res_dict[num+right_length] = cur_length
        return max_length
