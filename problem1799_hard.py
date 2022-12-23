# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/22 17:24
"""
from math import gcd
from typing import List

"""
给你 nums ，它是一个大小为 2 * n 的正整数数组。你必须对这个数组执行 n 次操作。
在第 i 次操作时（操作编号从 1 开始），你需要：
    选择两个元素 x 和 y 。
    获得分数 i * gcd(x, y) 。
    将 x 和 y 从 nums 中删除。
请你返回 n 次操作后你能获得的分数和最大为多少。
函数 gcd(x, y) 是 x 和 y 的最大公约数。

示例 1：
输入：nums = [1,2]
输出：1
解释：最优操作是：
(1 * gcd(1, 2)) = 1

示例 2：
输入：nums = [3,4,6,8]
输出：11
解释：最优操作是：
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

示例 3：
输入：nums = [1,2,3,4,5,6]
输出：14
解释：最优操作是：
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
"""
"""
思路：dp，首先计算任意两个数字之间的gcd，从小到大枚举所有状态，对于每个状态 k，先判断此状态中二进制位的个数 cnt 是否为偶数，
是则进行如下操作：枚举 k 中二进制位为 1 的位置，假设为 i 和 j，则 i 和 j 两个位置的元素可以进行一次操作，此时可以获得的分数为 
cnt/2×g[i][j]，更新 f[k] 的最大值。最终答案即为 f[2^m - 1]。
"""


class Solution:
    @staticmethod
    def maxScore(nums: List[int]) -> int:
        m = len(nums)
        g = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                g[i][j] = gcd(nums[i], nums[j])
        f = [0] * (1 << m)
        for k in range(1 << m):
            cnt = k.bit_count()
            if cnt % 2 == 0:
                for i in range(m):
                    if k >> i & 1:
                        for j in range(i + 1, m):
                            if k >> j & 1:
                                f[k] = max(f[k], f[k ^ (1 << i) ^ (1 << j)] + cnt // 2 * g[i][j])
        return f[-1]
