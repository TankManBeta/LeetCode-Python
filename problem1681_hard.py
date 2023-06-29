# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/28 20:37
"""
from cmath import inf
from typing import List

"""
给你一个整数数组 nums​​​ 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。
一个子集的 不兼容性 是该子集里面最大值和最小值的差。
请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。
子集的定义是数组中一些数字的集合，对数字顺序没有要求。 

示例 1：
输入：nums = [1,2,1,4], k = 2
输出：4
解释：最优的分配是 [1,2] 和 [1,4] 。
不兼容性和为 (2-1) + (4-1) = 4 。
注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。

示例 2：
输入：nums = [6,3,8,1,3,1,2,2], k = 4
输出：6
解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。

示例 3：
输入：nums = [5,3,3,6,3,3], k = 3
输出：-1
解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。
"""
"""
思路：我们可以枚举所有的子集 i，其中 i∈[0,2**n)，如果子集 i 的二进制表示中有 m 个 1，并且子集 i 中的元素没有重复，那么我们就
可以计算出子集 i 的不兼容性，记为 g[i]，即 g[i]=max{nums[j]}−min{nums[j]}。接下来，我们可以使用动态规划来求解。我们定义 f[i] 
表示当前已经划分的子集状态为 i 时，子集的不兼容性和的最小值。初始时 f[0]=0，表示没有任何元素被划分到子集中，其余 f[i]=+∞。
对于状态 i，我们找出所有未被划分且不重复的元素，用一个状态 mask 表示，如果状态 mask 中的元素个数大于等于 m，那么我们就枚举 mask 
的所有子集 j，并且满足 j⊂mask，那么 f[i∪j]=min{f[i∪j],f[i]+g[j]}。最后，如果 f[2**n−1]=+∞，那么说明无法划分成 k 个子集，
返回 −1，否则返回 f[2**n−1]。
"""


class Solution:
    @staticmethod
    def minimumIncompatibility(nums: List[int], k: int) -> int:
        n = len(nums)
        m = n // k
        g = [-1] * (1 << n)
        for i in range(1, 1 << n):
            if i.bit_count() != m:
                continue
            s = set()
            mi, mx = 20, 0
            for j, x in enumerate(nums):
                if i >> j & 1:
                    if x in s:
                        break
                    s.add(x)
                    mi = min(mi, x)
                    mx = max(mx, x)
            if len(s) == m:
                g[i] = mx - mi
        f = [inf] * (1 << n)
        f[0] = 0
        for i in range(1 << n):
            if f[i] == inf:
                continue
            s = set()
            mask = 0
            for j, x in enumerate(nums):
                if (i >> j & 1) == 0 and x not in s:
                    s.add(x)
                    mask |= 1 << j
            if len(s) < m:
                continue
            j = mask
            while j:
                if g[j] != -1:
                    f[i | j] = min(f[i | j], f[i] + g[j])
                j = (j - 1) & mask
        return f[-1] if f[-1] != inf else -1
