# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/14 22:00
"""
from collections import Counter
from typing import List

"""
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

示例 1：
输入：barcodes = [1,1,1,2,2,2]
输出：[2,1,2,1,2,1]

示例 2：
输入：barcodes = [1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]
"""
"""
思路：我们先用哈希表或数组 cnt 统计数组 barcodes 中各个数出现的次数，然后将 barcodes 中的数按照它们在 cnt 中出现的次数从大到小
排序，如果出现次数相同，那么就按照数的大小从小到大排序（确保相同的数相邻）。
接下来，我们创建一个长度为 n 的答案数组 ans，然后遍历排好序的 barcodes，将元素依次填入答案数组的 0,2,4,⋯ 等偶数下标位置，然后
将剩余元素依次填入答案数组的 1,3,5,⋯ 等奇数下标位置即可。
"""


class Solution:
    @staticmethod
    def rearrangeBarcodes(barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        barcodes.sort(key=lambda x: (-cnt[x], x))
        n = len(barcodes)
        ans = [0] * len(barcodes)
        ans[::2] = barcodes[: (n + 1) // 2]
        ans[1::2] = barcodes[(n + 1) // 2:]
        return ans
