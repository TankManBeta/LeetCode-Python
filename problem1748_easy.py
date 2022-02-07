# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/6 0:26
"""
"""
给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
请你返回 nums 中唯一元素的 和 。

输入：nums = [1,2,3,2]
输出：4
解释：唯一元素为 [1,3] ，和为 4 。

输入：nums = [1,1,1,1,1]
输出：0
解释：没有唯一元素，和为 0 。

输入：nums = [1,2,3,4,5]
输出：15
解释：唯一元素为 [1,2,3,4,5] ，和为 15 。
"""
"""
思路：
（1）两遍遍历，第一遍计数，第二遍求和
（2）一遍遍历，三种状态（0表示不存在，1表示存在一次，2表示多次存在）num的状态为0说明第一次存在，结果加上num，状态变为1；
如果num的状态为1说明之前已经存在一次，结果减去num，状态变为2；如果状态为2，说明之前已经多次存在，不需要额外操作
"""


class Solution(object):
    @staticmethod
    def sum_of_unique(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dict_num = {}
        # sum = 0
        # for num in nums:
        #     dict_num[num] = dict_num.get(num,0)+1
        # for key, count in dict_num.items():
        #     if count==1:
        #         sum += key*count
        # return sum

        dict_num = {}
        ans = 0
        for num in nums:
            if num not in dict_num.keys():
                ans += num
                dict_num[num] = 1
            elif dict_num[num] == 1:
                ans -= num
                dict_num[num] = 2
        return ans
