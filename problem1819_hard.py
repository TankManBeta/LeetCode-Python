# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/14 16:55
"""
from math import gcd
from typing import List

"""
给你一个由正整数组成的数组 nums 。
数字序列的 最大公约数 定义为序列中所有整数的共有约数中的最大整数。
例如，序列 [4,6,16] 的最大公约数是 2 。
数组的一个 子序列 本质是一个序列，可以通过删除数组中的某些元素（或者不删除）得到。
例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
计算并返回 nums 的所有 非空 子序列中 不同 最大公约数的 数目 。

示例 1：
输入：nums = [6,10,3]
输出：5
解释：上图显示了所有的非空子序列与各自的最大公约数。
不同的最大公约数为 6 、10 、3 、2 和 1 。

示例 2：
输入：nums = [5,15,40,5,6]
输出：7
"""
"""
思路：
（1）如果 x 为数组 nums 中的某个序列的最大公约数，则数组中所有能够被 x 整除的元素构成的最大公约数一定为 x 。根据上述结论，
我们可以枚举所有可能的最大公约数 x ，其中 x∈[1, max(nums)]，然后对数组中所有可以整除 x 的元素求最大公约数，判断最后求出的最大
公约数是否等于 x 即可。
（2）优化思路：<1>子序列的长度为 1，此时最大公约数等于 nums[i]，这部分可以给答案贡献 m 个，这里 m 为 nums 中不同元素的个数。
<2>子序列的长度至少为 2，为了避免重复统计，此时最大公约数 i 必须不在 nums 中。此外，要想使最大公约数为 i，nums 中最小要有 2i 
和 3i 这两个数，这样最大公约数才能是 i。因此，i 只需要枚举到 ⌊U/3⌋
"""


class Solution:
    @staticmethod
    def countDifferentSubsequenceGCDs(nums: List[int]) -> int:
        # ans, mx = 0, max(nums)
        # has = [False] * (mx + 1)
        # for x in nums:
        #     has[x] = True
        # for i in range(1, mx + 1):
        #     g = 0  # 0 和任何数 x 的最大公约数都是 x
        #     for j in range(i, mx + 1, i):  # 枚举 i 的倍数 j
        #         if has[j]:  # 如果 j 在 nums 中
        #             g = gcd(g, j)  # 更新最大公约数
        #             if g == i:  # 找到一个答案（g 无法继续减小）
        #                 ans += 1
        #                 break  # 提前退出循环
        # return ans

        ans, mx = 0, max(nums)
        has = [False] * (mx + 1)
        for x in nums:
            if not has[x]:
                has[x] = True
                ans += 1  # 单独一个数也算
        for i in range(1, mx // 3 + 1):  # 优化循环上界
            if has[i]:
                continue
            g = 0  # 0 和任何数 x 的最大公约数都是 x
            for j in range(i * 2, mx + 1, i):  # 枚举 i 的倍数 j
                if has[j]:  # 如果 j 在 nums 中
                    g = gcd(g, j)  # 更新最大公约数
                    if g == i:  # 找到一个答案（g 无法继续减小）
                        ans += 1
                        break  # 提前退出循环
        return ans
