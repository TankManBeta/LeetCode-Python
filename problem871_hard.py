# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/26 22:07
"""
from typing import List

"""
汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。
沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。
假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。
当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

示例 1：
输入：target = 1, startFuel = 1, stations = []
输出：0
解释：我们可以在不加油的情况下到达目的地。

示例 2：
输入：target = 100, startFuel = 1, stations = [[10,100]]
输出：-1
解释：我们无法抵达目的地，甚至无法到达第一个加油站。

示例 3：
输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
输出：2
解释：
我们出发时有 10 升燃料。
我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
我们沿途在1两个加油站停靠，所以返回 2 。
"""
"""
思路：用 n 表示数组 stations 的长度，即加油站的个数。最多可以加油 n 次，为了得到可以到达目的地的最少加油次数，需要计算每个加油
次数对应的最大行驶英里数，然后得到最大行驶英里数大于等于 target 的最少加油次数。
用 dp[i] 表示加油 i 次的最大行驶英里数。由于初始时汽油量是 startFuel 升，可以行驶 startFuel 英里，因此 dp[0]=startFuel。
当遍历到加油站 stations[i] 时，假设在到达该加油站之前已经加油 j 次，其中 0≤j≤i，则只有当 dp[j]≥stations[i][0] 时才能在加油 j 
次的情况下到达加油站 stations[i] 的位置，在加油站 stations[i] 加油之后，共加油 j+1 次，可以行驶的英里数是 dp[j]+stations[i][1]。
遍历满足 0≤j≤i 且 dp[j]≥stations[i][0] 的每个下标 j，计算 dp[j+1] 的最大值。
当遍历到加油站 stations[i] 时，对于每个符合要求的下标 j，计算 dp[j+1] 时都是将加油站 stations[i] 作为最后一次加油的加油站。
为了确保每个 dp[j+1] 的计算中，加油站 stations[i] 只会被计算一次，应该按照从大到小的顺序遍历下标 j。
"""


class Solution:
    @staticmethod
    def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (pos, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= pos:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        return next((i for i, v in enumerate(dp) if v >= target), -1)
