# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/16 13:34
"""
from typing import List

"""
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表
和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
求所能获得硬币的最大数量。

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

示例 2：
输入：nums = [1,5]
输出：10
"""
"""
思路：定义 f[l][r] 为考虑将 (l,r) 范围内（不包含 l 和 r 边界）的气球消耗掉，所能取得的最大价值。假设k是区间[i,j]之间最后一个
气球，则f[l][r]=f[l][k]+f[k][r]+arr[l]×arr[k]×arr[r]，所以我们遍历i和j之间的k即可。为了确保转移能够顺利进行，我们需要确保在
计算 f[l][r] 的时候，区间长度比其小的 f[l][k] 和 f[k][r] 均被计算。因此我们可以采用先枚举区间长度 len，然后枚举区间左端点 l
（同时直接算得区间右端点 r）的方式来做。
"""


class Solution:
    @staticmethod
    def maxCoins(nums: List[int]) -> int:

        # nums首尾添加1，方便处理边界情况
        nums.insert(0, 1)
        nums.insert(len(nums), 1)

        store = [[0] * (len(nums)) for _ in range(len(nums))]

        def range_best(i, j):
            m = 0
            # k是(i,j)区间内最后一个被戳的气球
            for k in range(i + 1, j):  # k取值在(i,j)开区间中
                # 以下都是开区间(i,k), (k,j)
                left = store[i][k]
                right = store[k][j]
                a = left + nums[i] * nums[k] * nums[j] + right
                if a > m:
                    m = a
            store[i][j] = m

        # 对每一个区间长度进行循环
        for n in range(2, len(nums)):  # 区间长度 #长度从3开始，n从2开始
            # 开区间长度会从3一直到len(nums)
            # 因为这里取的是range，所以最后一个数字是len(nums)-1

            # 对于每一个区间长度，循环区间开头的i
            for i in range(0, len(nums) - n):  # i+n = len(nums)-1

                # 计算这个区间的最多金币
                range_best(i, i + n)

        return store[0][len(nums) - 1]
