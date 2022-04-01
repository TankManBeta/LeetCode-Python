# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/31 16:08
"""
import random

"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""
"""
思路：
（1）直接排序取倒数第k个
（2）快排+分治，首先在left+1和right之间随机找一个数，left和i的数字交换作为pivot，是为了防止出现最坏情况，然后从left+1开始遍历，
如果nums[j]比pivot小的话就交换，全部遍历完之后，再把pivot和比pivot小的最右边界交换，这样j左边的比pivot小，右边的比pivot大。
然后判断j是否是自己想要的第k大的数，j比length-k说明在后面那一段，否则在前面那一段
"""


class Solution(object):
    @staticmethod
    def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # nums = sorted(nums, reverse=True)
        # return nums[k-1]

        def partition(left, right):
            if right > left:
                randomIndex = random.randint(left + 1, right)
                nums[left], nums[randomIndex] = nums[randomIndex], nums[left]
            pivot = nums[left]
            j = left
            for i in range(left + 1, right + 1):
                if nums[i] < pivot:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
            # 交换pivot比pivot小的最右边界的数
            nums[j], nums[left] = nums[left], nums[j]
            return j

        length = len(nums)
        l = 0
        r = length - 1
        target = length - k
        while True:
            index = partition(l, r)
            if index == target:
                return nums[index]
            elif index < target:
                l = index + 1
            else:
                r = index - 1
