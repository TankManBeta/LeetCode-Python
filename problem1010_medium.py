# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/7 14:24
"""
from collections import Counter
from typing import List

"""

"""
"""
思路：如果一个数对 (a,b) 之和能被 60 整除，即 (a+b)mod60=0，那么 (amod60+bmod60)mod60=0，不妨记 x=amod60, y=bmod60，那么有 
(x+y)mod60=0，即 y=(60−x)mod60。因此，我们可以遍历歌曲列表，用一个长度为 60 的数组 cnt 记录每个余数 x 出现的次数。对于当前的 
x，如果数组 cnt 中存在余数 y=(60−x)mod60，那么将 cnt[y] 累加进答案中。然后，将 x 在数组 cnt 中的出现次数加 1。继续遍历，直到
遍历完整个歌曲列表。
"""


class Solution:
    @staticmethod
    def numPairsDivisibleBy60(time: List[int]) -> int:
        cnt = Counter()
        ans = 0
        for x in time:
            x %= 60
            y = (60 - x) % 60
            ans += cnt[y]
            cnt[x] += 1
        return ans
