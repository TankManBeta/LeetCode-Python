# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/1 23:05
"""
from typing import List

"""
给你一个下标从 0 开始的整数数组 nums ，它表示英雄的能力值。如果我们选出一部分英雄，这组英雄的 力量 定义为：i0 ，i1 ，... ik 
表示这组英雄在数组中的下标。那么这组英雄的力量为 max(nums[i0],nums[i1] ... nums[ik])**2 * min(nums[i0],nums[i1] ... nums[ik]) 。
请你返回所有可能的 非空 英雄组的 力量 之和。由于答案可能非常大，请你将结果对 109 + 7 取余。 

示例 1：
输入：nums = [2,1,4]
输出：141
解释：
第 1 组：[2] 的力量为 22 * 2 = 8 。
第 2 组：[1] 的力量为 12 * 1 = 1 。
第 3 组：[4] 的力量为 42 * 4 = 64 。
第 4 组：[2,1] 的力量为 22 * 1 = 4 。
第 5 组：[2,4] 的力量为 42 * 2 = 32 。
第 6 组：[1,4] 的力量为 42 * 1 = 16 。
第​7 组：[2,1,4] 的力量为 42​* 1 = 16 。
所有英雄组的力量之和为 8 + 1 + 64 + 4 + 32 + 16 + 16 = 141 。

示例 2：
输入：nums = [1,1,1]
输出：7
解释：总共有 7 个英雄组，每一组的力量都是 1 。所以所有英雄组的力量之和为 7 。
"""
"""
思路：我们注意到，题目中涉及到子序列的最大值和最小值，数组中元素的顺序不影响最终的结果，因此我们可以先对数组进行排序。
接下来，我们枚举每个元素作为子序列的最小值，不妨记数组的每个元素为 a1,a2,⋯,an 。以 ai 作为最小值的子序列的贡献为：
ai×(ai**2+ai+1**2+2×ai+2**2+4×ai+3**2+⋯+2n−i−1×an**2)我们注意到，每一个 ai 都会乘上 ai**2 ，这一部分我们可以直接累加到答案中。
剩下的部分，我们可以用一个变量 p 来维护，初始时 p=0。接下来从右往左枚举 ai，每次我们将 ai ×p 累加到答案中，然后令 p=p×2+ai**2 。
枚举完所有的 ai 之后，返回答案即可。
"""


class Solution:
    @staticmethod
    def sumOfPower(nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        nums.sort()
        ans = 0
        p = 0
        for x in nums[::-1]:
            ans = (ans + (x * x % mod) * x) % mod
            ans = (ans + x * p) % mod
            p = (p * 2 + x * x) % mod
        return ans
