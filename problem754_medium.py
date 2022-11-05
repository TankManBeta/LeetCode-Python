# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/4 11:46
"""
"""
在一根无限长的数轴上，你站在0的位置。终点在target的位置。
你可以做一些数量的移动 numMoves :
每次你可以选择向左或向右移动。
第 i 次移动（从  i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。
给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves ) 。

示例 1:
输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。

示例 2:
输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。
"""
"""
思路：
（1）bfs，超时
（2）只有最后超出的步数k=sum-target为偶数时，才能通过在k/2处反向走实现消耗掉k的这个操作，因此分类讨论，如果sum==target，
直接能走到，如果k=sum-target为偶数，那么也能走到，如果k=sum-target为奇数，则需要分类讨论，目的是把k变成偶数即可，如果k+下一步
正好为偶数，就多走一次即可，否则多走两次
"""


class Solution:
    @staticmethod
    def reachNumber(target: int) -> int:
        # queue = [0]
        # move = 0
        # while queue:
        #     temp_queue = []
        #     for tmp in queue:
        #         if tmp == target:
        #             return move
        #         temp_queue.append(tmp+move+1)
        #         temp_queue.append(tmp-(move+1))
        #     move += 1
        #     queue = temp_queue

        target = abs(target)
        total = 0
        i = 1
        while True:
            total += i
            if total >= target and (total - target) % 2 == 0:
                return i
            i += 1
