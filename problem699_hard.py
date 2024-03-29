# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/18 19:40
"""
from typing import List

"""
在二维平面上的 x 轴上，放置着一些方块。
给你一个二维整数数组 positions ，其中 positions[i] = [lefti, sideLengthi] 表示：第 i 个方块边长为 sideLengthi ，其左侧边与 
x 轴上坐标点 lefti 对齐。
每个方块都从一个比目前所有的落地方块更高的高度掉落而下。方块沿 y 轴负方向下落，直到着陆到 另一个正方形的顶边 或者是 x 轴上 。
一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。一旦着陆，它就会固定在原地，无法移动。
在每个方块掉落后，你必须记录目前所有已经落稳的 方块堆叠的最高高度 。
返回一个整数数组 ans ，其中 ans[i] 表示在第 i 块方块掉落后堆叠的最高高度。

示例 1：
输入：positions = [[1,2],[2,3],[6,1]]
输出：[2,5,5]
解释：
第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 2 。
第 2 个方块掉落后，最高的堆叠由方块 1 和 2 组成，堆叠的最高高度为 5 。
第 3 个方块掉落后，最高的堆叠仍然由方块 1 和 2 组成，堆叠的最高高度为 5 。
因此，返回 [2, 5, 5] 作为答案。

示例 2：
输入：positions = [[100,100],[200,100]]
输出：[100,100]
解释：
第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 100 。
第 2 个方块掉落后，最高的堆叠可以由方块 1 组成也可以由方块 2 组成，堆叠的最高高度为 100 。
因此，返回 [100, 100] 作为答案。
注意，方块 2 擦过方块 1 的右侧边，但不会算作在方块 1 上着陆。
"""
"""
思路：我们用数组 heights 记录各个方块掉落后的高度。对于第 i 个掉落的方块，如果它的底部区间与第 j 个掉落的方块有重叠，那么它掉落
后的高度至少为 heights[j]+sizei，其中 j<i 且 sizei 为第 i 个掉落的方块的边长。因此对于第 i 个掉落的方块，heights[i] 的初始值为 
sizei，我们暴力枚举所有之前已经掉落的方块，如果两者的底部区间有重叠，那么更新 heights[i]=max(heights[i],heights[j]+sizei)。
"""


class Solution:
    @staticmethod
    def fallingSquares(positions: List[List[int]]) -> List[int]:
        n = len(positions)
        heights = [0] * n
        for i, (left1, side1) in enumerate(positions):
            right1 = left1 + side1 - 1
            heights[i] = side1
            for j in range(i):
                left2, right2 = positions[j][0], positions[j][0] + positions[j][1] - 1
                if right1 >= left2 and right2 >= left1:
                    heights[i] = max(heights[i], heights[j] + side1)
        for i in range(1, n):
            heights[i] = max(heights[i], heights[i - 1])
        return heights
