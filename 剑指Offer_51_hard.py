# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/14 23:15
"""
from typing import List

"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5
"""
"""
思路：合并阶段 本质上是 合并两个排序数组 的过程，而每当遇到 左子数组当前元素 > 右子数组当前元素 时，意味着 「左子数组当前元素 
至 末尾元素」 与 「右子数组当前元素」 构成了若干 「逆序对」 。
"""


class Solution:
    @staticmethod
    def reversePairs(nums: List[int]) -> int:
        def merge_sort(l, r):
            # 终止条件
            if l >= r:
                return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                if i == m + 1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1  # 统计逆序对
            return res

        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)
