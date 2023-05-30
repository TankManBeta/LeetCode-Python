# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/29 10:27
"""
"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下
移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1
"""
"""
思路：直接dfs，用一个visited记录访问过的地方即可
"""


class Solution:
    @staticmethod
    def movingCount(m: int, n: int, k: int) -> int:
        def convert(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        ans = 0
        visited = set()

        def dfs(x, y):
            if convert(x) + convert(y) > k:
                return
            nonlocal ans
            ans += 1
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited.add((x, y))
            for dir_x, dir_y in dirs:
                new_x, new_y = x + dir_x, y + dir_y
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                    dfs(new_x, new_y)

        dfs(0, 0)
        return ans
