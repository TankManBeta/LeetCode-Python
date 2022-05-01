# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/30 13:57
"""
"""
给你一个整数数组 nums，和一个整数 k 。
在一个操作中，您可以选择 0 <= i < nums.length 的任何索引 i 。将 nums[i] 改为 nums[i] + x ，其中 x 是一个范围为[-k, k]的整数。
对于每个索引 i ，最多 只能 应用 一次 此操作。
nums 的 分数 是 nums 中最大和最小元素的差值。 
在对  nums 中的每个索引最多应用一次上述操作后，返回 nums 的最低 分数 。

输入：nums = [1], k = 0
输出：0
解释：分数是 max(nums) - min(nums) = 1 - 1 = 0。

输入：nums = [0,10], k = 2
输出：6
解释：将 nums 改为 [2,8]。分数是 max(nums) - min(nums) = 8 - 2 = 6。

输入：nums = [1,3,6], k = 3
输出：0
解释：将 nums 改为 [4,4,4]。分数是 max(nums) - min(nums) = 4 - 4 = 0。
"""
"""
思路：如果本来差距大于2k，那么肯定不可能变成0，最多变成max-min-2k，否则变到0
"""


class Solution(object):
    @staticmethod
    def smallestRangeI(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_num = max(nums)
        min_num = min(nums)
        if max_num - min_num > 2*k:
            return max_num - min_num - 2*k
        else:
            return 0
