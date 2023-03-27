# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/26 15:34
"""
from typing import List

"""
假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。
然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于 一名年龄较大的球员，
则存在矛盾。同龄球员之间不会发生矛盾。
给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回 所有可能的无矛盾球队中得分最高那支的分数 。

示例 1：
输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
输出：34
解释：你可以选中所有球员。

示例 2：
输入：scores = [4,5,6,5], ages = [2,1,2,1]
输出：16
解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。

示例 3：
输入：scores = [1,2,3,5], ages = [8,9,10,1]
输出：6
解释：最佳的选择是前 3 名球员。
"""
"""
思路：我们可以将球员按照分数从小到大排序，如果分数相同，则按照年龄从小到大排序。接下来，使用动态规划求解。我们定义 f[i] 表示以
排序后的第 i 个球员作为最后一个球员的最大得分，那么答案就是 max(f[i]) 0≤i<n。
对于 f[i]，我们可以枚举 0≤j<i，如果第 i 个球员的年龄大于等于第 j 个球员的年龄，则 f[i] 可以从 f[j] 转移而来，转移方程为 
f[i]=max(f[i],f[j])。然后我们将第 i 个球员的分数加到 f[i] 中，即 f[i]+=scores[i]。最后，我们返回 max(f[i]) 即可。
"""


class Solution:
    @staticmethod
    def bestTeamScore(scores: List[int], ages: List[int]) -> int:
        arr = sorted(zip(scores, ages))
        n = len(arr)
        f = [0] * n
        for i, (score, age) in enumerate(arr):
            for j in range(i):
                if age >= arr[j][1]:
                    f[i] = max(f[i], f[j])
            f[i] += score
        return max(f)
