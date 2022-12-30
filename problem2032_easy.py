# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/29 20:25
"""
from typing import List

"""
给你三个整数数组 nums1、nums2 和 nums3 ，请你构造并返回一个 元素各不相同的 数组，且由 至少 在 两个 数组中出现的所有值组成。
数组中的元素可以按 任意 顺序排列。

示例 1：
输入：nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
输出：[3,2]
解释：至少在两个数组中出现的所有值为：
- 3 ，在全部三个数组中都出现过。
- 2 ，在数组 nums1 和 nums2 中出现过。

示例 2：
输入：nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
输出：[2,3,1]
解释：至少在两个数组中出现的所有值为：
- 2 ，在数组 nums2 和 nums3 中出现过。
- 3 ，在数组 nums1 和 nums2 中出现过。
- 1 ，在数组 nums1 和 nums3 中出现过。

示例 3：
输入：nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
输出：[]
解释：不存在至少在两个数组中出现的值。
"""
"""
思路：直接计数即可
"""


class Solution:
    @staticmethod
    def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # counter1 = [0]*101
        # counter2 = [0]*101
        # counter3 = [0]*101
        # ans = []
        # for num in nums1:
        #     counter1[num] = 1
        # for num in nums2:
        #     counter2[num] = 1
        # for num in nums3:
        #     counter3[num] = 1
        # for i in range(1, 101):
        #     count = counter1[i] + counter2[i] + counter3[i]
        #     if count >= 2:
        #         ans.append(i)
        # return ans

        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return [i for i in range(1, 101) if (i in s1) + (i in s2) + (i in s3) > 1]
