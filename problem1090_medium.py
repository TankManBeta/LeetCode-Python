# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/23 21:07
"""
from collections import Counter
from typing import List

"""
我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和 labels[i]。还会给出两个整数 numWanted 和 useLimit 。
从 n 个元素中选择一个子集 s :
    子集 s 的大小 小于或等于 numWanted 。
    s 中 最多 有相同标签的 useLimit 项。
    一个子集的 分数 是该子集的值之和。
返回子集 s 的最大 分数 。

示例 1：
输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
输出：9
解释：选出的子集是第一项，第三项和第五项。

示例 2：
输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
输出：12
解释：选出的子集是第一项，第二项和第三项。

示例 3：
输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
输出：16
解释：选出的子集是第一项和第四项。
"""
"""
思路：我们先将集合中的元素按照值从大到小进行排序，然后从前往后遍历排序后的元素。在遍历的过程中，我们使用一个哈希表 cnt 记录
每个标签出现的次数，如果某个标签出现的次数达到了 useLimit，那么我们就跳过该元素，否则我们就将该元素的值加到最终的答案中，
并将该标签出现的次数加 1。同时，我们用一个变量 num 记录当前子集中的元素个数，当 num 达到 numWanted 时，我们就可以结束遍历了。
"""


class Solution:
    @staticmethod
    def largestValsFromLabels(
            values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        ans = num = 0
        cnt = Counter()
        for v, l in sorted(zip(values, labels), reverse=True):
            if cnt[l] < useLimit:
                cnt[l] += 1
                num += 1
                ans += v
                if num == numWanted:
                    break
        return ans
