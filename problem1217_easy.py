# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/6 0:41
"""
from collections import Counter
from typing import List

"""
有 n 个筹码。第 i 个筹码的位置是 position[i] 。
我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:
    position[i] + 2 或 position[i] - 2 ，此时 cost = 0
    position[i] + 1 或 position[i] - 1 ，此时 cost = 1
返回将所有筹码移动到同一位置上所需要的 最小代价 。

示例 1：
输入：position = [1,2,3]
输出：1
解释：第一步:将位置3的筹码移动到位置1，成本为0。
第二步:将位置2的筹码移动到位置1，成本= 1。
总成本是1。

示例 2：
输入：position = [2,2,2,3,3]
输出：2
解释：我们可以把位置3的两个筹码移到位置2。每一步的成本为1。总成本= 2。

示例 3:
输入：position = [1,1000000000]
输出：1
"""
"""
思路：根据题意，奇数位置移动到奇数位置，代价为0。 奇数位置移动到偶数位置，代价为1。 偶数位置同理。 所以可以先将所有奇数位置的数
移动到一起，偶数位置的数移动到一起， 然后将两堆合并到一起，即求两堆的最小值。
"""


class Solution:
    @staticmethod
    def minCostToMoveChips(position: List[int]) -> int:
        cnt = Counter(p % 2 for p in position)  # 根据模 2 后的余数来统计奇偶个数
        return min(cnt[0], cnt[1])