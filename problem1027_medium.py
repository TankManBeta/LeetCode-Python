# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/22 16:15
"""
from typing import List

"""
给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。
回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。
并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。

示例 1：
输入：nums = [3,6,9,12]
输出：4
解释： 
整个数组是公差为 3 的等差数列。
示例 2：

输入：nums = [9,4,7,2,10]
输出：3
解释：
最长的等差子序列是 [4,7,10]。
示例 3：

输入：nums = [20,1,15,3,10,5,8]
输出：4
解释：
最长的等差子序列是 [20,15,10,5]。
"""
"""
思路：我们定义 f[i][j] 表示以 nums[i] 结尾且公差为 j 的等差数列的最大长度。初始时 f[i][j]=1，即每个元素自身都是一个长度为 1 
的等差数列。由于公差可能为负数，且最大差值为 500，因此，我们可以将统一将公差加上 500，这样公差的范围就变成了 [0,1000]。
考虑 f[i]，我们可以枚举 nums[i] 的前一个元素 nums[k]，那么公差 j=nums[i]−nums[k]+500，此时有 f[i][j]=max(f[i][j],f[k][j]+1)，
即我们可以从上一个转化过来，然后我们更新答案 ans=max(ans,f[i][j])。最后返回答案即可。
"""


class Solution:
    @staticmethod
    def longestArithSeqLength(nums: List[int]) -> int:
        n = len(nums)
        f = [[1] * 1001 for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for k in range(i):
                j = nums[i] - nums[k] + 500
                f[i][j] = max(f[i][j], f[k][j] + 1)
                ans = max(ans, f[i][j])
        return ans
