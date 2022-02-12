# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/11 10:26
"""
"""
给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。
从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。
返回可能的 最小差值 。

输入：nums = [90], k = 1
输出：0
解释：选出 1 名学生的分数，仅有 1 种方法：
- [90] 最高分和最低分之间的差值是 90 - 90 = 0
可能的最小差值是 0

输入：nums = [9,4,1,7], k = 2
输出：2
解释：选出 2 名学生的分数，有 6 种方法：
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 4 = 5
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 1 = 8
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 7 = 2
- [9,4,1,7] 最高分和最低分之间的差值是 4 - 1 = 3
- [9,4,1,7] 最高分和最低分之间的差值是 7 - 4 = 3
- [9,4,1,7] 最高分和最低分之间的差值是 7 - 1 = 6
可能的最小差值是 2
"""
"""
思路：先排序，然后维护一个长度为k的滑动窗口，比较nums[i+k-1]-nums[i]和min_gap的大小，小则更新
"""


class Solution(object):
    @staticmethod
    def minimum_difference(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        m = len(nums)
        min_gap = 10**5
        for i in range(0, m-k+1):
            if (nums[i+k-1]-nums[i]) < min_gap:
                min_gap = nums[i+k-1]-nums[i]
        return min_gap
