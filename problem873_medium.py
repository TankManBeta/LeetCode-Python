# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/26 20:50
"""
from typing import List

"""
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
    n >= 3
    对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
    给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
（回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。
例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）

示例 1：
输入: arr = [1,2,3,4,5,6,7,8]
输出: 5
解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。

示例 2：
输入: arr = [1,3,7,11,12,14,18]
输出: 3
解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
"""
"""
思路：当下标 i 确定时，任何小于下标 i 的下标 j 都可能满足 arr[j] 是某个斐波那契子序列中 arr[i] 前面的一个数字，因此只有当确定
斐波那契子序列的最后两个数字时，才能确定整个斐波那契子序列。定义二维数组 dp 表示以每个下标对的元素作为最后两个数字的斐波那契子
序列的最大长度。当 i>j 时，dp[j][i] 表示以 arr[j] 和 arr[i] 作为最后两个数字的斐波那契子序列的最大长度。初始时 dp 中的所有值
都是 0。为了计算 dp[j][i] 的值，需要得到该斐波那契序列中位于 arr[j] 前面的数字，该数字是 arr[i]−arr[j]。如果 arr[i]−arr[j] 
存在于数组 arr 中，且该数字小于 arr[j]，则用 k 表示其下标，有 arr[k]+arr[j]=arr[i]。因此在以 arr[k] 和 arr[j] 作为最后两个数
字的斐波那契子序列的后面添加 arr[i]，即可得到以 arr[j] 和 arr[i] 作为最后两个数字的斐波那契子序列。根据斐波那契子序列的定义可知，
斐波那契子序列的长度至少为 3。当 dp[k][j]≥3 时，dp[j][i]=dp[k][j]+1。当 dp[k][j]<3 时，以 arr[k] 和 arr[j] 作为最后两个数字的
斐波那契子序列并不存在，但是以 arr[j] 和 arr[i] 作为最后两个数字的斐波那契子序列存在，此时有 dp[j][i]=3。
"""


class Solution:
    @staticmethod
    def lenLongestFibSubsequence(arr: List[int]) -> int:
        indices = {x: i for i, x in enumerate(arr)}
        ans, n = 0, len(arr)
        dp = [[0] * n for _ in range(n)]
        for i, x in enumerate(arr):
            for j in range(n - 1, -1, -1):
                if arr[j] * 2 <= x:
                    break
                if x - arr[j] in indices:
                    k = indices[x - arr[j]]
                    dp[j][i] = max(dp[k][j] + 1, 3)
                    ans = max(ans, dp[j][i])
        return ans
