# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/20 21:45
"""
from cmath import inf
from typing import List

"""
给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 
nums[(i - 1 + n) % n] 。子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., 
nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。 

示例 1：
输入：nums = [1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3

示例 2：
输入：nums = [5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10

示例 3：
输入：nums = [3,-2,2,-3]
输出：3
解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
"""
"""
思路：求环形子数组的最大和，可以分为两种情况：情况一：最大和的子数组不包含环形部分，即为普通的最大子数组和；情况二：最大和的
子数组包含环形部分，我们可以转换为：求数组总和减去最小子数组和。因此，我们维护以下几个变量：前缀和最小值 pmi，初始值为 0；
前缀和最大值 pmx，初始值为 −∞；前缀和 s，初始值为 0；最小子数组和 smi，初始值为 ∞；答案 ans，初始值为 −∞。接下来，我们只需要
遍历数组 nums，对于当前遍历到的元素 x，我们做以下更新操作：更新前缀和 s=s+x；更新答案 ans=max(ans,s−pmi)，即为情况一的答案
（前缀和 s 减去最小前缀和 pmi，可以得到最大子数组和）；更新 smi=min(smi,s−pmx)，即为情况二的最小子数组和；更新 pmi=min(pmi,s)，
即为最小前缀和；更新 pmx=max(pmx,s)，即为最大前缀和。遍历结束，我们取 ans 以及 s−smi 的最大值作为答案返回即可。
"""


class Solution:
    @staticmethod
    def maxSubarraySumCircular(nums: List[int]) -> int:
        pmi, pmx = 0, -inf
        ans, s, smi = -inf, 0, inf
        for x in nums:
            s += x
            ans = max(ans, s - pmi)
            smi = min(smi, s - pmx)
            pmi = min(pmi, s)
            pmx = max(pmx, s)
        return max(ans, s - smi)
