# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/23 23:35
"""
from bisect import bisect_right
from collections import defaultdict
from typing import List

"""
给你一个无向图，无向图由整数 n  ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条无向边。
同时给你一个代表查询的整数数组 queries 。
第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目：
a < b
cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答案。
请注意，图中可能会有 重复边 。 

示例 1：
输入：n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
输出：[6,5]
解释：每个点对中，与至少一个点相连的边的数目如上图所示。
answers[0] = 6。所有的点对(a, b)中边数和都大于2，故有6个；
answers[1] = 5。所有的点对(a, b)中除了(3,4)边数等于3，其它点对边数和都大于3，故有5个。

示例 2：
输入：n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
输出：[10,10,9,8,6]
"""
"""
思路：根据题目，我们可以知道，与点对 (a,b) 相连的边数等于“与 a 相连的边数”加上“与 b 相连的边数”，再减去同时与 a 和 b 相连的边数。
因此，我们可以先用数组 cnt 统计与每个点相连的边数，用哈希表 g 统计每个点对的数量。然后，对于每个查询 q，我们可以枚举 a，对于每个 a，
我们可以通过二分查找找到第一个满足 cnt[a]+cnt[b]>q 的 b，先将数量累加到当前查询的答案中，然后减去一部分重复的边。
"""


class Solution:
    @staticmethod
    def countPairs(
            n: int, edges: List[List[int]], queries: List[int]
    ) -> List[int]:
        cnt = [0] * n
        g = defaultdict(int)
        for a, b in edges:
            a, b = a - 1, b - 1
            a, b = min(a, b), max(a, b)
            cnt[a] += 1
            cnt[b] += 1
            g[(a, b)] += 1

        s = sorted(cnt)
        ans = [0] * len(queries)
        for i, t in enumerate(queries):
            for j, x in enumerate(s):
                k = bisect_right(s, t - x, lo=j + 1)
                ans[i] += n - k
            for (a, b), v in g.items():
                if cnt[a] + cnt[b] > t >= cnt[a] + cnt[b] - v:
                    ans[i] -= 1
        return ans
