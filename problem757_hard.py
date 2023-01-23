# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/22 19:22
"""
from typing import List

"""
给你一个二维整数数组 intervals ，其中 intervals[i] = [starti, endi] 表示从 starti 到 endi 的所有整数，包括 starti 和 endi 。
包含集合 是一个名为 nums 的数组，并满足 intervals 中的每个区间都 至少 有 两个 整数在 nums 中。
例如，如果 intervals = [[1,3], [3,7], [8,9]] ，那么 [1,2,4,7,8,9] 和 [2,3,4,8,9] 都符合 包含集合 的定义。
返回包含集合可能的最小大小。

示例 1：
输入：intervals = [[1,3],[3,7],[8,9]]
输出：5
解释：nums = [2, 3, 4, 8, 9].
可以证明不存在元素数量为 4 的包含集合。

示例 2：
输入：intervals = [[1,3],[1,4],[2,5],[3,5]]
输出：3
解释：nums = [2, 3, 4].
可以证明不存在元素数量为 2 的包含集合。 

示例 3：
输入：intervals = [[1,2],[2,3],[2,4],[4,5]]
输出：5
解释：nums = [1, 2, 3, 4, 5].
可以证明不存在元素数量为 4 的包含集合。 
"""
"""
思路：首先对 intervals 按照 [s,e] 序对进行升序排序，然后我们需要额外记录每一个区间与最后交集集合中相交的元素（只记录到 m 个为止）。
同样我们从最后一个区间往前进行处理，如果该区间与交集集合相交元素个数小于 m 个时，我们从该区间左边界开始往后添加不在交集集合中的元素，
并往前进行更新需要更新的区间，重复该过程直至该区间与交集元素集合有 m 个元素相交。
"""


class Solution:
    @staticmethod
    def intersectionSizeTwo(intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, n, m = 0, len(intervals), 2
        values = [[] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            j = intervals[i][0]
            for _ in range(len(values[i]), m):
                ans += 1
                # 和其他区间有相交的元素也一并放进对应的区间，故而可以满足最小的约束
                for p in range(i - 1, -1, -1):
                    if intervals[p][1] < j:
                        break
                    values[p].append(j)
                j += 1
        return ans
