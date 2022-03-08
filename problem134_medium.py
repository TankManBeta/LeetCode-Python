# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/7 15:21
"""
"""
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第i+1个加油站需要消耗汽油cost[i]升。你从其中的一个加油站出发，开始时油箱为空。
给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则保证它是唯一的。

输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。

输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
"""
"""
思路：
（1）剩余总量最低点，如果最低点小于0，说明走不完一圈；否则index+1即为所求，因为前面损失的都能从index+1往后补回来
（2）从0开始，找最远能到达的位置记为i，则0-i之间的点作为起始点都不能绕行一圈，从i+1开始继续搜索
"""


class Solution(object):
    @staticmethod
    def can_complete_circuit(gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # min_index = -1
        # temp_remainder = 0
        # min_remainder = float("inf")
        # n = len(gas)
        # for i in range(n):
        #     temp_remainder += gas[i] - cost[i]
        #     if temp_remainder <= min_remainder:
        #         min_remainder = temp_remainder
        #         min_index = i
        # if temp_remainder < 0:
        #     return -1
        # return (min_index + 1) % n

        n = len(gas)
        i = 0
        while i < n:
            all_gas = 0
            all_cost = 0
            count = 0
            while count < n:
                j = (i + count) % n
                all_gas += gas[j]
                all_cost += cost[j]
                if all_gas < all_cost:
                    break
                count += 1
            if count == n:
                return i
            else:
                i = i + count + 1
        return -1

