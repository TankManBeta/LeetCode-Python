# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/26 11:55
"""
"""
给你一个下标从0开始的整数数组nums，该数组的大小为n，请你计算nums[j]-nums[i]能求得的最大差值，其中0<= i<j<n且nums[i]<nums[j]。
返回 最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 。

输入：nums = [7,1,5,4]
输出：4
解释：
最大差值出现在 i = 1 且 j = 2 时，nums[j] - nums[i] = 5 - 1 = 4 。
注意，尽管 i = 1 且 j = 0 时 ，nums[j] - nums[i] = 7 - 1 = 6 > 4 ，但 i > j 不满足题面要求，所以 6 不是有效的答案。

输入：nums = [9,4,3,2]
输出：-1
解释：
不存在同时满足 i < j 和 nums[i] < nums[j] 这两个条件的 i, j 组合。

输入：nums = [1,5,2,10]
输出：9
解释：
最大差值出现在 i = 0 且 j = 3 时，nums[j] - nums[i] = 10 - 1 = 9 。
"""
"""
思路：最大差值是当前数值减去左边最小的
"""


class Solution(object):
    @staticmethod
    def maximum_difference(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = 0
        m = len(nums)
        ans = -1
        for i in range(1, m):
            if (nums[i]-nums[small]) > ans and (nums[i]-nums[small]) != 0:
                ans = nums[i]-nums[small]
            if nums[i] < nums[small]:
                small = i
        return ans
