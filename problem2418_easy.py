# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/25 21:31
"""
from typing import List

"""
给你一个字符串数组 names ，和一个由 互不相同 的正整数组成的数组 heights 。两个数组的长度均为 n 。
对于每个下标 i，names[i] 和 heights[i] 表示第 i 个人的名字和身高。
请按身高 降序 顺序返回对应的名字数组 names 。

示例 1：
输入：names = ["Mary","John","Emma"], heights = [180,165,170]
输出：["Mary","Emma","John"]
解释：Mary 最高，接着是 Emma 和 John 。

示例 2：
输入：names = ["Alice","Bob","Bob"], heights = [155,185,150]
输出：["Bob","Alice","Bob"]
解释：第一个 Bob 最高，然后是 Alice 和第二个 Bob 。
"""
"""
思路：创建一个长度为 n 的下标数组 idx，其中 idx[i]=i。然后我们对 idx 中的每个下标按照 heights 中对应的身高降序排序，最后遍历
排序后的 idx 中的每个下标 i，将 names[i] 加入答案数组即可。
"""


class Solution:
    @staticmethod
    def sortPeople(names: List[str], heights: List[int]) -> List[str]:
        idx = list(range(len(heights)))
        idx.sort(key=lambda i: -heights[i])
        return [names[i] for i in idx]
