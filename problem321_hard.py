# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/13 15:05
"""
from typing import List

"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字
拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]

示例 2:
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]

示例 3:
输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
"""
"""
思路：问题其实总共分为两步，第一步是从nums1选k1个数，nums2选k2个数；第二步是将这k1+k2个数进行合并。首先第一步的解法是用一个
单调栈，因为要尽可能的是大数，所以越往前的数越大，整个数越大，所以用一个单调栈来判断，如果当前字符比栈顶元素大，就把栈顶的元素
弹出来，然后将当前字符入栈。第二步的解法就是合并，如果当前k1中的数字比k2中的大，就放大的那个；如果两个一样大的话需要比较后面
哪个大。
"""


class Solution:
    @staticmethod
    def maxNumber(nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_max_subsequence(nums: List[int], amount: int):
            stack = list()
            remain = len(nums) - amount
            for digit in nums:
                while stack and remain and stack[-1] < digit:
                    stack.pop()
                    remain -= 1
                stack.append(digit)
            return stack[:amount]

        def merge_sequence(arr1: List[int], arr2: List[int]):
            ans = []
            while arr1 or arr2:
                bigger = arr1 if arr1 > arr2 else arr2
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        m, n = len(nums1), len(nums2)
        max_sub = [0] * k
        start, end = max(0, k - n), min(k, m)
        for i in range(start, end + 1):
            sub1 = get_max_subsequence(nums1, i)
            sub2 = get_max_subsequence(nums2, k - i)
            cur_sub = merge_sequence(sub1, sub2)
            if cur_sub > max_sub:
                max_sub = cur_sub
        return max_sub
