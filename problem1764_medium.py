# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/17 14:02
"""
from typing import List

"""
给你一个长度为 n 的二维整数数组 groups ，同时给你一个整数数组 nums 。
你是否可以从 nums 中选出 n 个 不相交 的子数组，使得第 i 个子数组与 groups[i] （下标从 0 开始）完全相同，且如果 i > 0 ，
那么第 (i-1) 个子数组在 nums 中出现的位置在第 i 个子数组前面。（也就是说，这些子数组在 nums 中出现的顺序需要与 groups 顺序相同）
如果你可以找出这样的 n 个子数组，请你返回 true ，否则返回 false 。
如果不存在下标为 k 的元素 nums[k] 属于不止一个子数组，就称这些子数组是 不相交 的。子数组指的是原数组中连续元素组成的一个序列。

示例 1：
输入：groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
输出：true
解释：你可以分别在 nums 中选出第 0 个子数组 [1,-1,0,1,-1,-1,3,-2,0] 和第 1 个子数组 [1,-1,0,1,-1,-1,3,-2,0] 。
这两个子数组是不相交的，因为它们没有任何共同的元素。

示例 2：
输入：groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]
输出：false
解释：选择子数组 [1,2,3,4,10,-2] 和 [1,2,3,4,10,-2] 是不正确的，因为它们出现的顺序与 groups 中顺序不同。
[10,-2] 必须出现在 [1,2,3,4] 之前。

示例 3：
输入：groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]
输出：false
解释：选择子数组 [7,7,1,2,3,4,7,7] 和 [7,7,1,2,3,4,7,7] 是不正确的，因为它们不是不相交子数组。
它们有一个共同的元素 nums[4] （下标从 0 开始）。
"""
"""
思路：
（1）对groups中的每一个group进行匹配，返回在数组中的最后一个位置index，然后下一个匹配的范围是nums[index:]
（2）kmp算法
（3）双指针+贪心，就挨着匹配，匹配成功之后就匹配下一个
"""


class Solution:
    @staticmethod
    def canChoose(groups: List[List[int]], nums: List[int]) -> bool:
        # def match(list1, list2):
        #     m = len(list1)
        #     n = len(list2)
        #     index = -1
        #     i, j = 0, 0
        #     if m < n:
        #         return -1
        #     else:
        #         while i < m and j < n:
        #             if list1[i] == list2[j]:
        #                 i += 1
        #                 j += 1
        #             else:
        #                 i = i-j+1
        #                 j = 0
        #         if j == n:
        #             return i
        #     return index
        #
        # groups_len = sum([len(group) for group in groups])
        # nums_len = len(nums)
        # if groups_len > nums_len:
        #     return False
        # for group in groups:
        #     a = match(nums, group)
        #     if a == -1:
        #         return False
        #     else:
        #         nums = nums[a:]
        # return True

        k = 0
        for g in groups:
            while k + len(g) <= len(nums):
                if nums[k: k + len(g)] == g:
                    k += len(g)
                    break
                k += 1
            else:
                return False
        return True
