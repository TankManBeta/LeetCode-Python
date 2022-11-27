# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/26 16:14
"""
from typing import List

"""
爱丽丝和鲍勃拥有不同总数量的糖果。给你两个数组 aliceSizes 和 bobSizes ，aliceSizes[i] 是爱丽丝拥有的第 i 盒糖果中的糖果数量，
bobSizes[j] 是鲍勃拥有的第 j 盒糖果中的糖果数量。
两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果。一个人拥有的糖果总数量是他们每盒糖果数量的总和。
返回一个整数数组 answer，其中 answer[0] 是爱丽丝必须交换的糖果盒中的糖果的数目，answer[1] 是鲍勃必须交换的糖果盒中的糖果的数目。
如果存在多个答案，你可以返回其中 任何一个 。题目测试用例保证存在与输入对应的答案。

示例 1：
输入：aliceSizes = [1,1], bobSizes = [2,2]
输出：[1,2]

示例 2：
输入：aliceSizes = [1,2], bobSizes = [2,3]
输出：[1,2]

示例 3：
输入：aliceSizes = [2], bobSizes = [1,3]
输出：[2,3]

示例 4：
输入：aliceSizes = [1,2,5], bobSizes = [2,4]
输出：[5,4]
"""
"""
思路：sumA−x+y=sumB+x−y，然后化简一下，x=y+(sumA−sumB)//2，对于任意y，看x是否存在就行，用哈希表防止超时
"""


class Solution:
    @staticmethod
    def fairCandySwap(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # a = sum(aliceSizes)
        # b = sum(bobSizes)
        # m = len(aliceSizes)
        # n = len(bobSizes)
        # for i in range(m):
        #     for j in range(n):
        #         temp1 = aliceSizes[i] - bobSizes[j]
        #         temp2 = bobSizes[j] - aliceSizes[i]
        #         if a - temp1 == b - temp2:
        #             return [aliceSizes[i], bobSizes[j]]

        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        delta = (sumA - sumB) // 2
        rec = set(aliceSizes)
        ans = None
        for y in bobSizes:
            x = y + delta
            if x in rec:
                ans = [x, y]
                break
        return ans
