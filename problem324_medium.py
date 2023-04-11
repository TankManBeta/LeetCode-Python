# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/10 10:39
"""
import datetime
from random import seed, randint
from typing import List

"""
给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
你可以假设所有输入数组都可以得到满足题目要求的结果。 

示例 1：
输入：nums = [1,5,1,1,6,4]
输出：[1,6,1,5,1,4]
解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。

示例 2：
输入：nums = [1,3,2,2,3,1]
输出：[2,3,1,3,1,2]
"""
"""
思路：
（1）排序，首先将nums排序，然后将其分为前半部分呢和后半部分，然后依次选进行排序。这样会出现问题，例如对于[1,1,2,2,2,3]而言，
可以将其分割为[1,1,2]和[2,2,3]，最终结果为[1,2,1,2,2,3]，来自A的2和来自B的2出现在了相邻位置。我的解决办法就是在nums长度为偶数
时将分好的前后部分进行反序，然后再排列。nums长度为奇数时，这种情况是不存在有效解的，也就是说，这种数组对于本题来说是非法的。
（2）首先使用基于快速排序的快速选择选到第k小的数，然后进行三路划分（荷兰旗问题），然后再同（1）一样进行合并即可。
"""


# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         tmp = sorted(nums)
#         n = len(tmp)
#         idx = n // 2 if n % 2 == 0 else n // 2 + 1
#         left = tmp[:idx]
#         right = tmp[idx:]
#         n1 = len(left)
#         n2 = len(right)
#         if n1 == n2:
#             left = left[::-1]
#             right = right[::-1]
#         else:
#             nums[-1] = left[-1]
#         for i in range(n2):
#             nums[2*i] = left[i]
#             nums[2*i+1] = right[i]

class Helper:
    @staticmethod
    def quickSelect(arr: List, l: int, r: int, index: int) -> int:
        q = Helper.randomPartition(arr, l, r)
        if q == index:
            return arr[q]
        if q < index:
            return Helper.quickSelect(arr, q + 1, r, index)
        return Helper.quickSelect(arr, l, q - 1, index)

    @staticmethod
    def randomPartition(nums: List, l: int, r: int) -> int:
        i = randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return Helper.partition(nums, l, r)

    @staticmethod
    def partition(nums: List, l: int, r: int) -> int:
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1


class Solution:
    @staticmethod
    def wiggleSort(nums: List[int]) -> None:
        n = len(nums)
        x = (n + 1) // 2
        seed(datetime.datetime.now())
        target = Helper.quickSelect(nums, 0, n - 1, x - 1)
        k, i, j = 0, 0, n - 1
        while k <= j:
            if nums[k] > target:
                while j > k and nums[j] > target:
                    j -= 1
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            if nums[k] < target:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
            k += 1
        arr = nums.copy()
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                nums[i + 1] = arr[k]
            j -= 1
            k -= 1
