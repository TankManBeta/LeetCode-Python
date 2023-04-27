# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/26 9:25
"""
from itertools import accumulate
from typing import List

"""
给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个非重叠 子数组 中元素的最大和，长度分别为 firstLen 
和 secondLen 。
长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是不重叠的。
子数组是数组的一个 连续 部分。 

示例 1：
输入：nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
输出：20
解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。

示例 2：
输入：nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
输出：29
解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。

示例 3：
输入：nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
输出：31
解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
"""
"""
思路：首先预处理出前缀和数组，然后可能有两种情况，第一种是长度为firstLen的子数组在长度为secondLen的子数组的左边，所以我们枚举
secondLen子数组的左端点，用变量 t 维护左边 firstLen 个元素的子数组的最大和，那么当前最大和就是 t+s[i+secondLen]−s[i]；第二种
情况是长度为secondLen的子数组在长度为firstLen子数组的左边，用变量t维护左边 secondLen 个元素的子数组的最大和，同理可得当前最大和
就是 t+s[i+firstLen]−s[i] 。
"""


class Solution:
    @staticmethod
    def maxSumTwoNoOverlap(nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        ans = t = 0
        i = firstLen
        while i + secondLen - 1 < n:
            t = max(t, s[i] - s[i - firstLen])
            ans = max(ans, t + s[i + secondLen] - s[i])
            i += 1
        t = 0
        i = secondLen
        while i + firstLen - 1 < n:
            t = max(t, s[i] - s[i - secondLen])
            ans = max(ans, t + s[i + firstLen] - s[i])
            i += 1
        return ans
