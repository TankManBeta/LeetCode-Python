# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/19 13:00
"""
from typing import List

"""
有一个自行车手打算进行一场公路骑行，这条路线总共由 n + 1 个不同海拔的点组成。自行车手从海拔为 0 的点 0 开始骑行。
给你一个长度为 n 的整数数组 gain ，其中 gain[i] 是点 i 和点 i + 1 的 净海拔高度差（0 <= i < n）。请你返回 最高点的海拔 。

示例 1：
输入：gain = [-5,1,5,0,-7]
输出：1
解释：海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1 。

示例 2：
输入：gain = [-4,-3,-2,-1,4,3,2]
输出：0
解释：海拔高度依次为 [0,-4,-7,-9,-10,-6,-3,-1] 。最高海拔为 0 。
"""
"""
思路：求前缀和即可，反思一下自己的做法有点费空间，不过思路还是一样的。
"""


class Solution:
    @staticmethod
    def largestAltitude(gain: List[int]) -> int:
        # n = len(gain)
        # altitude = [0] * (n+1)
        # res = 0
        # for i in range(1, n+1):
        #     altitude[i] = altitude[i-1] + gain[i-1]
        #     res = max(res, altitude[i])
        # return res

        ans = total = 0
        for x in gain:
            total += x
            ans = max(ans, total)
        return ans
