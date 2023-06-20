# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/19 14:29
"""
from cmath import inf
from typing import List

"""
给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。 

示例 1：
输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。

示例 2：
输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以无法选出数字，返回 0。

示例 3：
输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
"""
"""
思路：
（1）贪心，首先计算出所有的和s，如果s是3的倍数直接return结果；在遍历过程中将模3余1和模3余2的数字分别放入a1，a2数组当中，然后看
s模3的结果，如果是1的话，则最后的结果是从s中减去a1[0]或者减去a2[0]+a2[1]，使得最后的余数变为0同时和最大。
（2）dp，我们定义 f[i][j] 表示前 i 个数中选取若干个数，使得这若干个数的和模 3 余 j 的最大值。初始时 f[0][0]=0，其余为 −∞。
对于 f[i][j]，我们可以考虑第 i 个数 x 的状态：
    如果我们不选 x，那么 f[i][j]=f[i−1][j]；
    如果我们选 x，那么 f[i][j]=f[i−1][(j−x%3+3)%3]+x。
因此我们可以得到状态转移方程：f[i][j]=max{f[i−1][j],f[i−1][(j−x%3+3)%3]+x}
"""


class Solution:
    @staticmethod
    def maxSumDivThree(nums: List[int]) -> int:
        # s = 0
        # a1, a2 = [], []
        # for num in nums:
        #     s += num
        #     if num % 3 == 1:
        #         a1.append(num)
        #     elif num % 3 == 2:
        #         a2.append(num)
        # if s % 3 == 0:
        #     return s
        # a1 = sorted(a1)
        # a2 = sorted(a2)
        # if s % 3 == 2:
        #     a1, a2 = a2, a1
        # ans = s - a1[0] if a1 else 0
        # if len(a2) > 1:
        #     ans = max(ans, s - a2[0] - a2[1])
        # return ans

        n = len(nums)
        f = [[-inf] * 3 for _ in range(n + 1)]
        f[0][0] = 0
        for i, x in enumerate(nums, 1):
            for j in range(3):
                f[i][j] = max(f[i - 1][j], f[i - 1][(j - x) % 3] + x)
        return f[n][0]
