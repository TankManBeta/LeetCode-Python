# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/9 13:49
"""
"""
给你一个偶数 n ，已知存在一个长度为 n 的排列 perm ，其中 perm[i] == i​（下标 从 0 开始 计数）。
一步操作中，你将创建一个新数组 arr ，对于每个 i ：
    如果 i % 2 == 0 ，那么 arr[i] = perm[i / 2]
    如果 i % 2 == 1 ，那么 arr[i] = perm[n / 2 + (i - 1) / 2]
    然后将 arr​​ 赋值​​给 perm 。
要想使 perm 回到排列初始值，至少需要执行多少步操作？返回最小的 非零 操作步数。

示例 1：
输入：n = 2
输出：1
解释：最初，perm = [0,1]
第 1 步操作后，perm = [0,1]
所以，仅需执行 1 步操作

示例 2：
输入：n = 4
输出：2
解释：最初，perm = [0,1,2,3]
第 1 步操作后，perm = [0,2,1,3]
第 2 步操作后，perm = [0,1,2,3]
所以，仅需执行 2 步操作

示例 3：
输入：n = 6
输出：4
"""
"""
思路：
（1）直接模拟即可，看从perm到perm需要多少步
（2）对模拟进行优化，思路1枚举了所有位置进行交换，但其实我们不用枚举所有位置。通过分析可以发现，所有的数交换后会构成一个环，
每个环经过它长度的交换后就回会到最初的状态，那么我们求出最大的环的长度(可以发现必然是所有环的最小公倍数），经过在这个长度的交换，
所有数必然回到最初的位置。我们可以直到1或n-2肯定在最大环中，所以只需要模拟1即可，也就是每次回溯上一步索引，直到回到1即可。
（3）新数组的偶数位数字依次是原数组的前半段数字；新数组的奇数位数字依次是原数组的后半段数字。原来前半部分的i变为2i，后半部分的i
变成2i−(n−1)，然后进行模拟即可。
"""


class Solution:
    @staticmethod
    def reinitializePermutation(n: int) -> int:
        # origin = [i for i in range(n)]
        # perm = [i for i in range(n)]
        # ans = 0
        # while True:
        #     arr = [0]*n
        #     for i in range(n):
        #         if i % 2 == 0:
        #             arr[i] = perm[i//2]
        #         else:
        #             arr[i] = perm[n // 2 + (i - 1) // 2]
        #     ans += 1
        #     if arr == origin:
        #         return ans
        #     else:
        #         perm = arr

        # i = 1
        # ans = 0
        # while True:
        #     if i % 2 == 0:
        #         i = i // 2
        #     else:
        #         i = (n + i - 1) // 2
        #     ans += 1
        #     if i == 1:
        #         return ans

        i = 1
        ans = 0
        while True:
            if i < n >> 1:
                i = i * 2
            else:
                i = 2 * i - n + 1
            ans += 1
            if i == 1:
                return ans
