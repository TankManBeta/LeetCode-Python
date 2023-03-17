# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/16 10:06
"""
from collections import Counter
from typing import List

"""
给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。
统计并返回 nums 中的 中位数 等于 k 的非空子数组的数目。
注意：
数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
子数组是数组中的一个连续部分。 

示例 1：
输入：nums = [3,2,1,4,5], k = 4
输出：3
解释：中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。

示例 2：
输入：nums = [2,3,1], k = 3
输出：1
解释：[3] 是唯一一个中位数等于 3 的子数组。
"""
"""
思路：首先ans=1，因为自己单独一个数字肯定是一个答案。找到k在nums中的index，然后从index往后维护一个x，x的意思是index往后比k大的
数和比k小的数的差值，也就是说如果nums[i]>k，那么x++，否则x--，如果x==0或x==-1则满足题设条件，则ans++，同时cnt[x]++，这个cnt是
记录同一个差值存在的数量，方便跨index的子数组的统计。现在从index往左维护一个x，步骤同上，只是在统计时需要考虑跨index的子区间，
所以只需要加上cnt[-x]（左边比k大的数和比k小的数的差值是x，所以右边比k小的数与比k大的数差值需要是-x，所以找cnt[-x]的个数即为
答案的数量）和cnt[-x+1]（同理。子数组长度为偶数时，取中间靠左为中位数的情况）即可。
"""


class Solution:
    @staticmethod
    def countSubarrays(nums: List[int], k: int) -> int:
        ans = 1
        n = len(nums)
        cnt = Counter()
        index = nums.index(k)
        x = 0
        for i in range(index + 1, n):
            if nums[i] > k:
                x += 1
            else:
                x -= 1
            if x == 0 or x == 1:
                ans += 1
            cnt[x] += 1
        x = 0
        for j in range(index - 1, -1, -1):
            if nums[j] > k:
                x += 1
            else:
                x -= 1
            if x == 0 or x == 1:
                ans += 1
            ans += cnt[-x] + cnt[-x + 1]
        return ans
