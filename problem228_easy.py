# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/11 10:39
"""
"""
给定一个  无重复元素 的 有序 整数数组 nums 。
返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个
范围但不属于 nums 的数字 x 。
列表中的每个区间范围 [a,b] 应该按如下格式输出：
    "a->b" ，如果 a != b
    "a" ，如果 a == b

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""
"""
思路：一次遍历，如果当前和下一位的差值为1就继续temp++，然后判断temp和i的大小关系，如果i和temp相等就说明是独立的数，否则就是一个
区间
"""


class Solution(object):
    @staticmethod
    def summaryRanges(nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        i = 0
        while i < n:
            temp = i
            while temp+1<n and nums[temp+1] == nums[temp]+1:
                temp += 1
            if i == temp:
                res.append("{}".format(nums[temp]))
            else:
                res.append("{}->{}".format(nums[i], nums[temp]))
            i = temp+1
        return res
