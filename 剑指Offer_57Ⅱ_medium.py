# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/8 20:54
"""
"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。 

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""
"""
思路：
（1）在确定了i的情况下，可以根据求和公式求出j的值。
（2）双指针，设连续正整数序列的左边界 i 和右边界 j ，则可构建滑动窗口从左向右滑动。循环中，每轮判断滑动窗口内元素和与目标值 
target 的大小关系，若相等则记录结果，若大于 target 则移动左边界 i （以减小窗口内的元素和），若小于 target 则移动右边界 j 
（以增大窗口内的元素和）。
"""


class Solution:
    @staticmethod
    def findContinuousSequence(target: int):
        # i, j, res = 1, 2, []
        # while i < j:
        #     j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
        #     if i < j and j == int(j):
        #         res.append(list(range(i, int(j) + 1)))
        #     i += 1
        # return res

        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res
