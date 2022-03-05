# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/4 11:03
"""
"""
给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
返回nums中所有子数组范围的和 。
子数组是数组中一个连续 非空 的元素序列。

输入：nums = [1,2,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0 
[2]，范围 = 2 - 2 = 0
[3]，范围 = 3 - 3 = 0
[1,2]，范围 = 2 - 1 = 1
[2,3]，范围 = 3 - 2 = 1
[1,2,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4

输入：nums = [1,3,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0
[3]，范围 = 3 - 3 = 0
[3]，范围 = 3 - 3 = 0
[1,3]，范围 = 3 - 1 = 2
[3,3]，范围 = 3 - 3 = 0
[1,3,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4

输入：nums = [4,-2,-3,4,1]
输出：59
解释：nums 中所有子数组范围的和是 59
"""
"""
思路：
（1）暴力
（2）单调栈，对于nums中的每一个num，使用单调栈维护当前数字在其左边和右边担当最大值最小值的最远下标
"""


class Solution(object):
    @staticmethod
    def sub_array_ranges(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     max_num, min_num = nums[i], nums[i]
        #     for j in range(i, n):
        #         max_num = max(nums[j], max_num)
        #         min_num = min(nums[j], min_num)
        #         ans += (max_num - min_num)
        # return ans

        n = len(nums)
        # 记录当前值在左侧当最小值和最大值的最大位置
        min_left, max_left = [0] * n, [0] * n
        # 单调栈记录左侧最小值最大值的位置下标
        min_left_stack, max_left_stack = [], []
        for i, num in enumerate(nums):
            while min_left_stack and nums[min_left_stack[-1]] > num:
                min_left_stack.pop()
            min_left[i] = min_left_stack[-1] if min_left_stack else -1
            min_left_stack.append(i)
            while max_left_stack and nums[max_left_stack[-1]] <= num:
                max_left_stack.pop()
            max_left[i] = max_left_stack[-1] if max_left_stack else -1
            max_left_stack.append(i)

        # 记录当前值在右侧当最小值和最大值的最大位置
        min_right, max_right = [0] * n, [0] * n
        # 单调栈记录右侧最小值最大值的位置下标
        min_right_stack, max_right_stack = [], []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            while min_right_stack and nums[min_right_stack[-1]] >= num:
                min_right_stack.pop()
            min_right[i] = min_right_stack[-1] if min_right_stack else n
            min_right_stack.append(i)
            while max_right_stack and nums[max_right_stack[-1]] < num:
                max_right_stack.pop()
            max_right[i] = max_right_stack[-1] if max_right_stack else n
            max_right_stack.append(i)

        max_sum, min_sum = 0, 0
        for i, num in enumerate(nums):
            max_sum += (i - max_left[i]) * (max_right[i] - i) * num
            min_sum += (i - min_left[i]) * (min_right[i] - i) * num
        return max_sum - min_sum
