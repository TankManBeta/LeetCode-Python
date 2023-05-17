# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 11:09
"""
from math import inf
from typing import List

"""
你需要制定一份 d 天的工作计划表。工作之间存在依赖，要想执行第 i 项工作，你必须完成全部 j 项工作（ 0 <= j < i）。
你每天 至少 需要完成一项任务。工作计划的总难度是这 d 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。
给你一个整数数组 jobDifficulty 和一个整数 d，分别代表工作难度和需要计划的天数。第 i 项工作的难度是 jobDifficulty[i]。
返回整个工作计划的 最小难度 。如果无法制定工作计划，则返回 -1 。 

示例 1：
输入：jobDifficulty = [6,5,4,3,2,1], d = 2
输出：7
解释：第一天，您可以完成前 5 项工作，总难度 = 6.
第二天，您可以完成最后一项工作，总难度 = 1.
计划表的难度 = 6 + 1 = 7 

示例 2：
输入：jobDifficulty = [9,9,9], d = 4
输出：-1
解释：就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。

示例 3：
输入：jobDifficulty = [1,1,1], d = 3
输出：3
解释：工作计划为每天一项工作，总难度为 3 。

示例 4：
输入：jobDifficulty = [7,1,7,1,7,1], d = 3
输出：15

示例 5：
输入：jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
输出：843
"""
"""
思路：这一题思路比较容易想到，定义dp[i][j]为完成前i项工作分配到j天的最小工作难度，所以对于dp[i][j]来说，我们只需要枚举一个k
答案就为min(dp[i][j], dp[k-1][j-1]+mx)，也就是说，我们将前k-1项工作分配到j-1天，剩下的i-k项工作的最大值就为第j天的最大工作
难度。其中我们在枚举的时候可以从后往前枚举更新最大值，比从前往后更方便。
"""


class Solution:
    @staticmethod
    def minDifficulty(jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n == d:
            return sum(jobDifficulty)
        elif n < d:
            return -1
        else:
            dp = [[inf] * (d + 1) for _ in range(n + 1)]
            dp[0][0] = 0
            for i in range(1, n+1):
                for j in range(1, d+1):
                    mx = 0
                    for k in range(i, 0, -1):
                        mx = max(mx, jobDifficulty[k-1])
                        dp[i][j] = min(dp[i][j], dp[k-1][j-1]+mx)
            return dp[-1][-1]