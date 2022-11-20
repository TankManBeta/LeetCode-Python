# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/19 13:58
"""
from typing import List

"""
你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。
你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。
如果你能使这个正方形，则返回 true ，否则返回 false 。

示例 1:
输入: matchsticks = [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。

示例 2:
输入: matchsticks = [3,3,3,3,4]
输出: false
解释: 不能用所有火柴拼成一个正方形。
"""
"""
思路：如果火柴长度之和不为4的倍数则肯定不能拼成正方形；如果长度为4的倍数就dfs每一条边，如果该边当前长度加上新的长度仍然小于边长，
就dfs下一层，否则就dfs下一条边
"""


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        if totalLen % 4:
            return False
        target = totalLen//4
        matchsticks.sort(reverse=True)
        self.ans = False
        edges = [0] * 4
        def dfs(idx: int) -> bool:
            if self.ans or idx == len(matchsticks) and edges[0]==edges[1]==edges[2]==edges[3]==target:
                self.ans = True
                return
            if edges[0] + matchsticks[idx] <= target:
                edges[0] += matchsticks[idx]
                dfs(idx+1)
                edges[0] -= matchsticks[idx]
            if edges[1] + matchsticks[idx] <= target:
                edges[1] += matchsticks[idx]
                dfs(idx+1)
                edges[1] -= matchsticks[idx]
            if edges[2] + matchsticks[idx] <= target:
                edges[2] += matchsticks[idx]
                dfs(idx+1)
                edges[2] -= matchsticks[idx]
            if edges[3] + matchsticks[idx] <= target:
                edges[3] += matchsticks[idx]
                dfs(idx+1)
                edges[3] -= matchsticks[idx]
        dfs(0)
        return self.ans

        # matchsticks.sort(reverse = True)
        # if sum(matchsticks) % 4 != 0:
        #     return False
        # target = sum(matchsticks) // 4
        # @lru_cache(None)
        # def dfs(a, b, c, d, i):
        #     if i == len(matchsticks) and a == b == c == d == target:
        #         return True
        #     ret = False
        #     if a + matchsticks[i] <= target:
        #         ret = ret or dfs(a + matchsticks[i], b, c, d, i + 1)
        #     if b + matchsticks[i] <= target:
        #         ret = ret or dfs(a, b + matchsticks[i], c, d, i + 1)
        #     if c + matchsticks[i] <= target:
        #         ret = ret or dfs(a, b, c + matchsticks[i], d, i + 1)
        #     if d + matchsticks[i] <= target:
        #         ret = ret or dfs(a, b, c, d + matchsticks[i], i + 1)
        #     return ret
        # return dfs(0, 0, 0, 0, 0)