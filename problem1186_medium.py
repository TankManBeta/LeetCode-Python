# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/27 20:25
"""
from typing import List

"""
给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。换句话说，你可以从
原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组
（剩下）的元素总和是所有子数组之中最大的。
注意，删除一个元素后，子数组 不能为空。

示例 1：
输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。

示例 2：
输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，这就是最大和。

示例 3：
输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。
"""
"""
思路：
（1）预处理 + 枚举。我们可以先预处理出数组 arr 以每个元素结尾和开头的最大子数组和，分别存入数组 left 和 right 中。如果我们
不删除任何元素，那么最大子数组和就是 left[i] 或 right[i] 中的最大值；如果我们删除一个元素，我们可以枚举 [1..n−2] 中的每个
位置 i，计算 left[i−1]+right[i+1] 的值，取最大值即可。
（2）我们以 dp[i][k] 表示以 arr[i] 结尾，删除 k 次的非空子数组的最大和（删除前的末尾元素为 arr[i]，就视为以 arr[i] 结尾）。
初始时 dp[0][0]=arr[0]，dp[0][1]＝0（以 arr[0] 结尾，删除一次的非空子数组不存在，因此 dp[0][1] 不会计入结果）。当 i>0 时，
转移方程如下：dp[i][0]=max(dp[i−1][0],0)+arr[i]；dp[i][1]=max(dp[i−1][1]+arr[i],dp[i−1][0])。
"""


class Solution:
    @staticmethod
    def maximumSum(arr: List[int]) -> int:
        # n = len(arr)
        # left = [0] * n
        # right = [0] * n
        # s = 0
        # for i, x in enumerate(arr):
        #     s = max(s, 0) + x
        #     left[i] = s
        # s = 0
        # for i in range(n - 1, -1, -1):
        #     s = max(s, 0) + arr[i]
        #     right[i] = s
        # ans = max(left)
        # for i in range(1, n - 1):
        #     ans = max(ans, left[i - 1] + right[i + 1])
        # return ans

        dp0, dp1, res = arr[0], 0, arr[0]
        for i in range(1, len(arr)):
            dp1 = max(dp0, dp1 + arr[i])
            dp0 = max(dp0, 0) + arr[i]
            res = max(res, max(dp0, dp1))
        return res
