# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/17 19:34
"""
from collections import Counter
from typing import List

"""
给你一个数组 nums ，数组中只包含非负整数。定义 rev(x) 的值为将整数 x 各个数字位反转得到的结果。比方说 rev(123) = 321 ， 
rev(120) = 21 。我们称满足下面条件的下标对 (i, j) 是 好的 ：
    0 <= i < j < nums.length
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
请你返回好下标对的数目。由于结果可能会很大，请将结果对 109 + 7 取余 后返回。

示例 1：
输入：nums = [42,11,1,97]
输出：2
解释：两个坐标对为：
 - (0,3)：42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121 。
 - (1,2)：11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12 。
 
示例 2：
输入：nums = [13,10,35,24,76]
输出：4
"""
"""
思路：
（1）直接暴力按题目模拟，超时
（2）现在我们设：f(i)=nums[i]−rev(nums[i])，则题目中好下标对可以等价于：f(i)=f(j)。那么我们从左到右遍历数组 nums，并在遍历的
过程用「哈希表」统计每一个位置 0≤i<n 的 f(i) 的个数，则对于位置 0≤j<n，以 j 结尾的「好下标对」的个数为此时「哈希表」中 f(j) 
的数目。那么我们只需要在遍历时同时统计以每一个位置为结尾的「好下标对」数目即可。
"""


class Solution:
    @staticmethod
    def countNicePairs(nums: List[int]) -> int:
        # ans = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + int(str(nums[j])[::-1]) == nums[j] + int(str(nums[i])[::-1]):
        #             ans += 1
        # return ans % (10**9+7)

        counter = Counter()
        ans = 0
        for num in nums:
            reversed_num = int(str(num)[::-1])
            ans += counter[num - reversed_num]
            counter[num - reversed_num] += 1
        return ans % (10 ** 9 + 7)
