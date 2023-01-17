# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/16 20:32
"""
"""
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，
则返回 -1 。注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

示例 1：
输入：n = 12
输出：21

示例 2：
输入：n = 21
输出：-1
"""
"""
思路：我们希望找到一种方法，能够找到一个大于当前序列的新序列，且变大的幅度尽可能小。首先从后向前查找第一个顺序对 (i,i+1)，满足 
a[i]<a[i+1]。这样「较小数」即为 a[i]。此时 [i+1,n) 必然是下降序列。如果找到了顺序对，那么在区间 [i+1,n) 中从后向前查找第一个元素 
j 满足 a[i]<a[j]。这样「较大数」即为 a[j]。交换 a[i] 与 a[j]，此时可以证明区间 [i+1,n) 必为降序。我们可以直接使用双指针反转区间
[i+1,n) 使其变为升序，而无需对该区间进行排序。
"""


class Solution:
    @staticmethod
    def nextGreaterElement(n: int) -> int:
        nums = list(str(n))
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return -1

        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
        ans = int(''.join(nums))
        return ans if ans < 2 ** 31 else -1
