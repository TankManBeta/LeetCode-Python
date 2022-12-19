# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/18 14:39
"""
from itertools import accumulate
from typing import List

"""
给你一个整数数组 nums 和一个整数 k 。 nums 仅包含 0 和 1 。每一次移动，你可以选择 相邻 两个数字并将它们交换。
请你返回使 nums 中包含 k 个 连续 1 的 最少 交换次数。

示例 1：
输入：nums = [1,0,0,1,0,1], k = 2
输出：1
解释：在第一次操作时，nums 可以变成 [1,0,0,0,1,1] 得到连续两个 1 。

示例 2：
输入：nums = [1,0,0,0,0,0,1,1], k = 3
输出：5
解释：通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,1,1,1] 。

示例 3：
输入：nums = [1,1,0,1], k = 2
输出：0
解释：nums 已经有连续 2 个 1 了。
"""
"""
思路：
（1）找出所有满足条件的窗口，条件是窗口内正好有k个1，且窗口两个端点都是1；对每一个窗口，求出把其中k个1移到一块的最小cost并更新
全局最优解minCost。
给定窗口如何求最优解，常规想法是将1全都移动到一起，但是比较复杂，此时我们可以反过来想，我们将0全都移动到两端。移动右两种选择，
向左和向右，此时只需要判断哪个步骤移动的代价小就选哪个，也就是看当前0左边和右边1的个数。
思路优化：
    （1）合并连续的0，对于连续的0，它们的cost都是一样的，那么我们就可以把加法变乘法
    （2）cost如何求，就用i*zeros[i]求和即可
    （3）窗口滑动之后新的cost怎么求，我们可以注意到：在nums上，窗口长度是变化的；而在zeros上，窗口长度则是固定的。将窗口右滑后，
        前半部分的cost都减少了，比如原来cost为2的点右滑之后cost变为1；同理，后半部分的cost都增加了，然后按照这种规律对上一步的
        cost进行操作即可
（2）可以通过数学方法证明将所有的1移动到p[k/2]是最优的
"""


class Solution:
    @staticmethod
    def minMoves(nums: List[int], k: int) -> int:
        # def getZeros(start, nums):
        #     # 从start位置开始，生成1之间的zero个数的数组
        #     i = start
        #     n = len(nums)
        #     zeros = []
        #     # 过滤掉第一个1之前所有的0
        #     while i < n and nums[i] == 0:
        #         i += 1
        #     # 快慢指针统计1之间0的个数
        #     j = i + 1
        #     while j < n:
        #         # 如果当前位置不为0，即为1，则统计1之前的0的个数
        #         if nums[j] != 0:
        #             zeros.append(j - i - 1)
        #             # i移动到j位置，统计下一个区间的0的个数
        #             i = j
        #         j += 1
        #     return zeros

        # def getPreVector(zeros):
        #     # 构造前缀求和数组，该数字比输入数字多1，即前面多个0
        #     pres = [0]
        #     for i in range(len(zeros)):
        #         pres.append(pres[i] + zeros[i])
        #     return pres

        # def getRangeNum(left, right, pres):
        #     # 返回区间[left,right]的和
        #     return pres[right+1] - pres[left]
        # # 获得zeros数组
        # zeros = getZeros(0, nums)
        # # 计算第一个窗口的解
        # minCost = 0
        # for i in range(0, k-1):
        #     minCost += zeros[i] * min(i+1, k-i-1)
        # pres = getPreVector(zeros)
        # tempCost = minCost
        # # 滑动zeros窗口, 注意是以k-1大小的窗口滑动，因为k个1中间有k-1个缝隙存0
        # for w in range(1, len(zeros)-k+2):
        #     # 记录左右区间位置
        #     left = w; right = w + k - 2
        #     # 计算mid时用当前位置和末尾位置
        #     mid = (left + right) // 2
        #     # 而计算消耗变化时，要用前一个位置和末尾位置
        #     tempCost -= getRangeNum(left-1, mid-1, pres)
        #     tempCost += getRangeNum(mid+k%2, right, pres)
        #     minCost = min(minCost, tempCost)
        # return int(minCost)

        p = [q - i for i, q in enumerate(i for i, x in enumerate(nums) if x)]
        s = list(accumulate(p, initial=0))  # p 的前缀和
        return min(s[i] + s[i + k] - s[i + k // 2] * 2 - p[i + k // 2] * (k % 2)
                   for i in range(len(p) - k + 1))  # p[i:i+k] 中所有数到 p[i+k//2] 的距离之和，取最小值
