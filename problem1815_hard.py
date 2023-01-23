# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/22 18:56
"""
from linecache import cache
from typing import List

"""
有一个甜甜圈商店，每批次都烤batchSize个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前所有甜甜圈都必须已经全部销售完毕。
给你一个整数batchSize和一个整数数组groups，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中groups[i]表示这一批顾客的人数。
每一位顾客都恰好只要一个甜甜圈。当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客
得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。你可以随意安排每批顾客到来的顺序。请你返回在此前提下，最多有多少组人会感到
开心。 

示例 1：
输入：batchSize = 3, groups = [1,2,3,4,5,6]
输出：4
解释：你可以将这些批次的顾客顺序安排为 [6,2,4,5,1,3] 。那么第 1，2，4，6 组都会感到开心。

示例 2：
输入：batchSize = 4, groups = [1,3,2,5,2,2,1,6]
输出：4
"""
"""
思路：题目实际上要我们找到一种安排顺序，使得前缀和与batchSize 取模后为 0 的组数最多。
人数为 batchSize 的整数倍的顾客，这些顾客不会对下一组顾客的甜甜圈产生影响，我们可以贪心地优先安排这些组的顾客，那么这些组的顾客
都会感到开心，“初始答案”为这些组的数量；
人数不为 batchSize 的整数倍的顾客，这些顾客的安排顺序会影响下一组顾客的甜甜圈。我们可以对这里每一组的人数 v 模 batchSize，得到
的这些余数构成一个集合，集合中的元素值范围是 [1,2...,batchSize−1]。数组 groups 的长度最大为 30，因此，每个余数的数量最大不超过 
30。我们可以用 5 个二进制位来表示一个余数的数量，而 batchSize 最大为 9，那么表示这些余数以及对应的数量总共需要的二进制位就是 
5×(9−1)=40。我们可以用一个 64 位整数 state 来表示。
我们枚举 1 到 batchSize−1 的每一个余数 i，如果余数 i 的数量不为 0，那么我们可以将余数 i 的数量减去 1，将当前前缀余数加上 i 并
对 batchSize 取模，然后递归调用函数 dfs，求出子状态的最优解，取最大值即可。最后判断 mod 是否为 0，如果为 0，我们在最大值上加 1 
后返回，否则直接返回最大值。过程中，我们可以使用记忆化搜索来避免状态的重复计算。
"""


class Solution:
    @staticmethod
    def maxHappyGroups(batchSize: int, groups: List[int]) -> int:
        @cache
        def dfs(state, mod):
            res = 0
            x = int(mod == 0)
            for i in range(1, batchSize):
                if state >> (i * 5) & 31:
                    t = dfs(state - (1 << (i * 5)), (mod + i) % batchSize)
                    res = max(res, t + x)
            return res

        state = ans = 0
        for v in groups:
            i = v % batchSize
            ans += i == 0
            if i:
                state += 1 << (i * 5)
        ans += dfs(state, 0)
        return ans
