# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/9 0:48
"""
"""
给你一个整数数组 nums 和一个整数 k ，请你返回数对 (i, j) 的数目，满足 i < j 且 |nums[i] - nums[j]| == k 。
|x| 的值定义为：
    如果 x >= 0 ，那么值为 x 。
    如果 x < 0 ，那么值为 -x 。

输入：nums = [1,2,2,1], k = 1
输出：4
解释：差的绝对值为 1 的数对为：
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]

输入：nums = [1,3], k = 3
输出：0
解释：没有任何数对差的绝对值为 3 。

输入：nums = [3,2,1,5,4], k = 2
输出：3
解释：差的绝对值为 2 的数对为：
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]
"""
"""
思路：
（1）暴力，两遍循环
（2）一遍循环，每次ans+=num_dict.get(num-k, 0) + num_dict.get(num+k, 0)， 因为有i<j的条件，所以只需要统计当前位置之前的满足
条件的即可，后面的由后面的num保证
"""


class Solution(object):
    @staticmethod
    def count_k_difference(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # num_len = len(nums)
        # ans = 0
        # for i in range(num_len):
        #     for j in range(i+1, num_len):
        #         if nums[i]-nums[j]==k or nums[i]-nums[j] == -k:
        #             ans += 1
        # return ans

        num_dict = {}
        ans = 0
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            ans += num_dict.get(num - k, 0) + num_dict.get(num + k, 0)
        return ans
